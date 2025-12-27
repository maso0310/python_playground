"""
Python Playground - 教學用 Python 程式碼執行平台
讓六個組別可以在網頁上輸入並執行 Python 程式碼
"""

from flask import Flask, render_template, request, jsonify
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
import subprocess
import sys
import tempfile
import os
from datetime import datetime

real_app = Flask(__name__)

# 儲存各組的程式碼和執行結果
groups_data = {
    1: {"code": "", "output": "", "task": "", "last_run": None, "history": []},
    2: {"code": "", "output": "", "task": "", "last_run": None, "history": []},
    3: {"code": "", "output": "", "task": "", "last_run": None, "history": []},
    4: {"code": "", "output": "", "task": "", "last_run": None, "history": []},
    5: {"code": "", "output": "", "task": "", "last_run": None, "history": []},
    6: {"code": "", "output": "", "task": "", "last_run": None, "history": []},
}

# 預設任務列表（靜態執行版本）
default_tasks = {
    1: "【密碼產生器】產生 5 組隨機密碼，每組包含大小寫字母和數字，長度為 12 位",
    2: "【二分搜尋】電腦隨機產生 1-100 的答案，然後用二分法自動猜測，印出每次猜測的過程",
    3: "【圖形繪製】用 * 符號印出一棵高度為 10 的聖誕樹（三角形加樹幹）",
    4: "【撲克牌】模擬洗牌並抽出 5 張牌，判斷牌型（同花、順子、葫蘆等）",
    5: "【摩斯密碼】將 'HELLO WORLD' 轉換成摩斯密碼，並將摩斯密碼轉回英文驗證",
    6: "【統計模擬】模擬擲 2 顆骰子 10000 次，統計並印出每種點數和（2-12）的出現次數和機率",
}

# 初始化任務
for group_id, task in default_tasks.items():
    groups_data[group_id]["task"] = task


@real_app.route("/")
def index():
    """主頁面 - 顯示六個組別的程式編輯區"""
    return render_template("index.html", groups_data=groups_data)


@real_app.route("/run/<int:group_id>", methods=["POST"])
def run_code(group_id):
    """執行指定組別的 Python 程式碼"""
    if group_id not in groups_data:
        return jsonify({"error": "無效的組別"}), 400

    data = request.get_json()
    code = data.get("code", "")

    # 儲存程式碼
    groups_data[group_id]["code"] = code
    groups_data[group_id]["last_run"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 建立暫存檔案執行程式碼
    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as f:
            f.write(code)
            temp_file = f.name

        # 執行程式碼，設定超時時間為 10 秒
        result = subprocess.run(
            [sys.executable, temp_file],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=os.path.dirname(temp_file)
        )

        output = result.stdout
        if result.stderr:
            output += "\n[錯誤訊息]\n" + result.stderr

        os.unlink(temp_file)

    except subprocess.TimeoutExpired:
        output = "[執行超時] 程式執行超過 10 秒，已被終止"
        os.unlink(temp_file)
    except Exception as e:
        output = f"[系統錯誤] {str(e)}"

    groups_data[group_id]["output"] = output

    return jsonify({
        "output": output,
        "last_run": groups_data[group_id]["last_run"]
    })


@real_app.route("/save/<int:group_id>", methods=["POST"])
def save_code(group_id):
    """儲存指定組別的程式碼（不執行）"""
    if group_id not in groups_data:
        return jsonify({"error": "無效的組別"}), 400

    data = request.get_json()
    code = data.get("code", "")
    groups_data[group_id]["code"] = code

    return jsonify({"message": "程式碼已儲存"})


@real_app.route("/task/<int:group_id>", methods=["POST"])
def update_task(group_id):
    """更新指定組別的任務，並將舊任務存入歷史"""
    if group_id not in groups_data:
        return jsonify({"error": "無效的組別"}), 400

    data = request.get_json()
    new_task = data.get("task", "")
    save_history = data.get("save_history", True)  # 預設儲存歷史

    group = groups_data[group_id]

    # 如果有舊任務且有程式碼或輸出，儲存到歷史紀錄
    if save_history and group["task"] and (group["code"] or group["output"]):
        history_entry = {
            "task": group["task"],
            "code": group["code"],
            "output": group["output"],
            "completed_at": group["last_run"] or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        group["history"].append(history_entry)

    # 更新為新任務，清除目前的程式碼和輸出
    group["task"] = new_task
    group["code"] = ""
    group["output"] = ""
    group["last_run"] = None

    return jsonify({"message": "任務已更新", "history_count": len(group["history"])})


@real_app.route("/all_tasks", methods=["POST"])
def update_all_tasks():
    """批量更新所有組別的任務，並儲存歷史"""
    data = request.get_json()
    tasks = data.get("tasks", {})
    save_history = data.get("save_history", True)

    for group_id, task in tasks.items():
        gid = int(group_id)
        if gid in groups_data:
            group = groups_data[gid]

            # 儲存歷史紀錄
            if save_history and group["task"] and (group["code"] or group["output"]):
                history_entry = {
                    "task": group["task"],
                    "code": group["code"],
                    "output": group["output"],
                    "completed_at": group["last_run"] or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                group["history"].append(history_entry)

            # 更新任務並清除目前資料
            group["task"] = task
            group["code"] = ""
            group["output"] = ""
            group["last_run"] = None

    return jsonify({"message": "所有任務已更新"})


@real_app.route("/get_all_data")
def get_all_data():
    """取得所有組別的資料"""
    return jsonify(groups_data)


@real_app.route("/history/<int:group_id>")
def get_history(group_id):
    """取得指定組別的歷史紀錄"""
    if group_id not in groups_data:
        return jsonify({"error": "無效的組別"}), 400

    return jsonify({
        "group_id": group_id,
        "history": groups_data[group_id]["history"]
    })


@real_app.route("/overview")
def overview():
    """全班總覽頁面 - 查看各組執行狀況與歷史紀錄"""
    return render_template("overview.html", groups_data=groups_data)


@real_app.route("/admin")
def admin():
    """管理者頁面 - 用於指派任務"""
    return render_template("admin.html", groups_data=groups_data)


@real_app.route("/clear/<int:group_id>", methods=["POST"])
def clear_group(group_id):
    """清除指定組別的程式碼和輸出"""
    if group_id not in groups_data:
        return jsonify({"error": "無效的組別"}), 400

    groups_data[group_id]["code"] = ""
    groups_data[group_id]["output"] = ""
    groups_data[group_id]["last_run"] = None

    return jsonify({"message": "已清除"})


# 使用 DispatcherMiddleware 將應用掛載到 /python_playground 路徑
app = DispatcherMiddleware(
    lambda environ, start_response: (
        start_response('404 Not Found', [('Content-Type', 'text/plain')]) or [b'Not Found']
    ),
    {
        "/python_playground": real_app
    }
)


if __name__ == "__main__":
    run_simple("0.0.0.0", 5000, app, use_reloader=True, use_debugger=True)
