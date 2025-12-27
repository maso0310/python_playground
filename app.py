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
import threading
import queue
import time
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

# 互動式程序的狀態
interactive_sessions = {}

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


class InteractiveSession:
    """管理互動式 Python 程序的類別"""

    def __init__(self, group_id, code):
        self.group_id = group_id
        self.code = code
        self.process = None
        self.temp_file = None
        self.output_queue = queue.Queue()
        self.output_history = []
        self.is_running = False
        self.waiting_for_input = False
        self.reader_thread = None

    def start(self):
        """啟動互動式程序"""
        # 建立暫存檔案
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as f:
            f.write(self.code)
            self.temp_file = f.name

        # 啟動程序
        self.process = subprocess.Popen(
            [sys.executable, "-u", self.temp_file],  # -u 禁用緩衝
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            cwd=os.path.dirname(self.temp_file)
        )

        self.is_running = True

        # 啟動讀取輸出的線程
        self.reader_thread = threading.Thread(target=self._read_output, daemon=True)
        self.reader_thread.start()

        return True

    def _read_output(self):
        """在背景線程中讀取程序輸出"""
        try:
            while self.is_running and self.process.poll() is None:
                line = self.process.stdout.readline()
                if line:
                    self.output_queue.put(line)
                    self.output_history.append(line)

            # 讀取剩餘的輸出
            remaining = self.process.stdout.read()
            if remaining:
                self.output_queue.put(remaining)
                self.output_history.append(remaining)

        except Exception as e:
            self.output_queue.put(f"\n[系統錯誤] {str(e)}\n")
        finally:
            self.is_running = False

    def send_input(self, user_input):
        """發送輸入給程序"""
        if self.process and self.process.poll() is None:
            try:
                self.process.stdin.write(user_input + "\n")
                self.process.stdin.flush()
                return True
            except Exception as e:
                return False
        return False

    def get_output(self):
        """取得新的輸出"""
        output_lines = []
        while not self.output_queue.empty():
            try:
                output_lines.append(self.output_queue.get_nowait())
            except queue.Empty:
                break
        return "".join(output_lines)

    def get_full_output(self):
        """取得完整的輸出歷史"""
        return "".join(self.output_history)

    def is_active(self):
        """檢查程序是否仍在運行"""
        if self.process:
            return self.process.poll() is None
        return False

    def stop(self):
        """停止程序"""
        self.is_running = False
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=2)
            except:
                try:
                    self.process.kill()
                except:
                    pass

        # 清理暫存檔案
        if self.temp_file and os.path.exists(self.temp_file):
            try:
                os.unlink(self.temp_file)
            except:
                pass


@real_app.route("/")
def index():
    """主頁面 - 顯示六個組別的程式編輯區"""
    return render_template("index.html", groups_data=groups_data)


@real_app.route("/run/<int:group_id>", methods=["POST"])
def run_code(group_id):
    """執行指定組別的 Python 程式碼（一次性執行）"""
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


# ===== 互動模式 API =====

@real_app.route("/interactive/start/<int:group_id>", methods=["POST"])
def interactive_start(group_id):
    """啟動互動式程序"""
    if group_id not in groups_data:
        return jsonify({"error": "無效的組別"}), 400

    # 停止已有的 session
    if group_id in interactive_sessions:
        interactive_sessions[group_id].stop()

    data = request.get_json()
    code = data.get("code", "")

    if not code.strip():
        return jsonify({"error": "請先輸入程式碼"}), 400

    # 儲存程式碼
    groups_data[group_id]["code"] = code
    groups_data[group_id]["last_run"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 建立新的 session
    session = InteractiveSession(group_id, code)

    try:
        session.start()
        interactive_sessions[group_id] = session

        # 等待一下讓程序有機會輸出
        time.sleep(0.1)

        return jsonify({
            "success": True,
            "message": "互動模式已啟動",
            "output": session.get_output()
        })
    except Exception as e:
        return jsonify({"error": f"啟動失敗: {str(e)}"}), 500


@real_app.route("/interactive/input/<int:group_id>", methods=["POST"])
def interactive_input(group_id):
    """發送輸入給互動式程序"""
    if group_id not in interactive_sessions:
        return jsonify({"error": "互動模式未啟動"}), 400

    session = interactive_sessions[group_id]

    if not session.is_active():
        return jsonify({
            "error": "程式已結束",
            "output": session.get_output(),
            "finished": True
        })

    data = request.get_json()
    user_input = data.get("input", "")

    # 發送輸入
    session.send_input(user_input)

    # 等待輸出
    time.sleep(0.15)

    return jsonify({
        "success": True,
        "output": session.get_output(),
        "running": session.is_active()
    })


@real_app.route("/interactive/output/<int:group_id>")
def interactive_output(group_id):
    """取得互動式程序的輸出"""
    if group_id not in interactive_sessions:
        return jsonify({"error": "互動模式未啟動", "running": False})

    session = interactive_sessions[group_id]

    return jsonify({
        "output": session.get_output(),
        "full_output": session.get_full_output(),
        "running": session.is_active()
    })


@real_app.route("/interactive/stop/<int:group_id>", methods=["POST"])
def interactive_stop(group_id):
    """停止互動式程序"""
    if group_id in interactive_sessions:
        session = interactive_sessions[group_id]
        full_output = session.get_full_output()
        session.stop()
        del interactive_sessions[group_id]

        # 儲存輸出
        groups_data[group_id]["output"] = full_output

        return jsonify({
            "success": True,
            "message": "互動模式已停止",
            "output": full_output
        })

    return jsonify({"success": True, "message": "沒有正在執行的程式"})


# ===== 其他 API =====

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
    """取得所有組別的資料"""
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

    # 停止互動式程序
    if group_id in interactive_sessions:
        interactive_sessions[group_id].stop()
        del interactive_sessions[group_id]

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
    run_simple("0.0.0.0", 5000, app, use_reloader=True, use_debugger=True, threaded=True)
