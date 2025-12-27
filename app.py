"""
Python Playground - 教學用 Python 程式碼執行平台
讓六個組別可以在網頁上輸入並執行 Python 程式碼
"""

from flask import Flask, render_template, request, jsonify
import subprocess
import sys
import tempfile
import os
import json
from datetime import datetime

app = Flask(__name__)

# 儲存各組的程式碼和執行結果
groups_data = {
    1: {"code": "", "output": "", "task": "", "last_run": None},
    2: {"code": "", "output": "", "task": "", "last_run": None},
    3: {"code": "", "output": "", "task": "", "last_run": None},
    4: {"code": "", "output": "", "task": "", "last_run": None},
    5: {"code": "", "output": "", "task": "", "last_run": None},
    6: {"code": "", "output": "", "task": "", "last_run": None},
}

# 預設任務列表
default_tasks = {
    1: "請寫一個程式，計算 1 到 100 的總和",
    2: "請寫一個程式，印出九九乘法表",
    3: "請寫一個程式，判斷一個數字是否為質數",
    4: "請寫一個程式，將華氏溫度轉換為攝氏溫度",
    5: "請寫一個程式，計算一個列表中的最大值和最小值",
    6: "請寫一個程式，反轉一個字串",
}

# 初始化任務
for group_id, task in default_tasks.items():
    groups_data[group_id]["task"] = task


@app.route("/")
def index():
    """主頁面 - 顯示六個組別的程式編輯區"""
    return render_template("index.html", groups_data=groups_data)


@app.route("/run/<int:group_id>", methods=["POST"])
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


@app.route("/save/<int:group_id>", methods=["POST"])
def save_code(group_id):
    """儲存指定組別的程式碼（不執行）"""
    if group_id not in groups_data:
        return jsonify({"error": "無效的組別"}), 400

    data = request.get_json()
    code = data.get("code", "")
    groups_data[group_id]["code"] = code

    return jsonify({"message": "程式碼已儲存"})


@app.route("/task/<int:group_id>", methods=["POST"])
def update_task(group_id):
    """更新指定組別的任務"""
    if group_id not in groups_data:
        return jsonify({"error": "無效的組別"}), 400

    data = request.get_json()
    task = data.get("task", "")
    groups_data[group_id]["task"] = task

    return jsonify({"message": "任務已更新"})


@app.route("/all_tasks", methods=["POST"])
def update_all_tasks():
    """批量更新所有組別的任務"""
    data = request.get_json()
    tasks = data.get("tasks", {})

    for group_id, task in tasks.items():
        gid = int(group_id)
        if gid in groups_data:
            groups_data[gid]["task"] = task

    return jsonify({"message": "所有任務已更新"})


@app.route("/get_all_data")
def get_all_data():
    """取得所有組別的資料（用於展示成果）"""
    return jsonify(groups_data)


@app.route("/showcase")
def showcase():
    """成果展示頁面 - 顯示所有組別的程式碼和執行結果"""
    return render_template("showcase.html", groups_data=groups_data)


@app.route("/admin")
def admin():
    """管理者頁面 - 用於指派任務"""
    return render_template("admin.html", groups_data=groups_data)


@app.route("/clear/<int:group_id>", methods=["POST"])
def clear_group(group_id):
    """清除指定組別的程式碼和輸出"""
    if group_id not in groups_data:
        return jsonify({"error": "無效的組別"}), 400

    groups_data[group_id]["code"] = ""
    groups_data[group_id]["output"] = ""
    groups_data[group_id]["last_run"] = None

    return jsonify({"message": "已清除"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
