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
import json
from datetime import datetime

real_app = Flask(__name__)

# 儲存各組的程式碼和執行結果
groups_data = {
    1: {"code": "", "output": "", "task": "", "last_run": None, "user_input": ""},
    2: {"code": "", "output": "", "task": "", "last_run": None, "user_input": ""},
    3: {"code": "", "output": "", "task": "", "last_run": None, "user_input": ""},
    4: {"code": "", "output": "", "task": "", "last_run": None, "user_input": ""},
    5: {"code": "", "output": "", "task": "", "last_run": None, "user_input": ""},
    6: {"code": "", "output": "", "task": "", "last_run": None, "user_input": ""},
}

# 預設任務列表
default_tasks = {
    1: "【密碼產生器】寫一個程式，產生一組包含大小寫字母和數字的 8 位隨機密碼",
    2: "【猜數字遊戲】寫一個程式，隨機產生 1-100 的數字，讓使用者猜測並給予提示（太大/太小）",
    3: "【文字藝術】寫一個程式，將使用者輸入的文字轉換成由 * 符號組成的大型字母（至少做 A-Z）",
    4: "【撲克牌抽牌】寫一個程式，模擬一副撲克牌洗牌後抽出 5 張牌，並判斷是否為同花、順子等牌型",
    5: "【摩斯密碼】寫一個程式，可以將英文句子轉換成摩斯密碼，也可以將摩斯密碼轉回英文",
    6: "【骰子遊戲】寫一個程式，模擬擲 2 顆骰子 1000 次，統計每種點數組合出現的機率",
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
    user_input = data.get("user_input", "")

    # 儲存程式碼和輸入
    groups_data[group_id]["code"] = code
    groups_data[group_id]["user_input"] = user_input
    groups_data[group_id]["last_run"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 建立暫存檔案執行程式碼
    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as f:
            f.write(code)
            temp_file = f.name

        # 執行程式碼，設定超時時間為 10 秒
        # 將 user_input 作為標準輸入傳給程式
        result = subprocess.run(
            [sys.executable, temp_file],
            input=user_input,
            capture_output=True,
            text=True,
            timeout=10,
            cwd=os.path.dirname(temp_file)
        )

        output = result.stdout
        if result.stderr:
            output += "\n[錯誤訊息]\n" + result.stderr

        # 刪除暫存檔案
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
    """更新指定組別的任務"""
    if group_id not in groups_data:
        return jsonify({"error": "無效的組別"}), 400

    data = request.get_json()
    task = data.get("task", "")
    groups_data[group_id]["task"] = task

    return jsonify({"message": "任務已更新"})


@real_app.route("/all_tasks", methods=["POST"])
def update_all_tasks():
    """批量更新所有組別的任務"""
    data = request.get_json()
    tasks = data.get("tasks", {})

    for group_id, task in tasks.items():
        gid = int(group_id)
        if gid in groups_data:
            groups_data[gid]["task"] = task

    return jsonify({"message": "所有任務已更新"})


@real_app.route("/get_all_data")
def get_all_data():
    """取得所有組別的資料（用於展示成果）"""
    return jsonify(groups_data)


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
    groups_data[group_id]["user_input"] = ""
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
    # 使用 run_simple 來運行 DispatcherMiddleware
    run_simple("0.0.0.0", 5000, app, use_reloader=True, use_debugger=True)
