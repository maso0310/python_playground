"""
Python Playground - 教學用 Python 程式碼執行平台
讓六個組別可以選擇題目並執行 Python 程式碼
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

# 題目類別名稱
CATEGORIES = {
    1: "基礎練習",
    2: "演算法",
    3: "圖形輸出",
    4: "資料處理",
    5: "模擬實驗",
    6: "綜合挑戰"
}

# 所有題目（按類別分組，每類別6題）
TASKS = {
    1: {  # 基礎練習
        1: "【變數練習】宣告姓名、年齡、身高三個變數，並印出自我介紹",
        2: "【計算機】計算 123 + 456、789 - 123、12 * 34、100 / 7 的結果",
        3: "【字串操作】將 'Hello World' 轉成大寫、小寫、反轉，並計算長度",
        4: "【列表操作】建立 1-10 的列表，印出總和、平均、最大、最小值",
        5: "【字典練習】建立一個學生資料字典（姓名、學號、成績），並印出內容",
        6: "【迴圈練習】用 for 迴圈印出 1-100 中所有 3 的倍數"
    },
    2: {  # 演算法
        1: "【二分搜尋】電腦隨機產生 1-100 的答案，用二分法自動猜測並印出過程",
        2: "【排序比較】產生 10 個隨機數字，分別用氣泡排序和選擇排序印出過程",
        3: "【費氏數列】印出費氏數列前 20 項，並計算第 20 項的值",
        4: "【質數篩選】找出 1-100 之間所有的質數",
        5: "【最大公因數】實作輾轉相除法，計算 48 和 18 的最大公因數",
        6: "【河內塔】印出 4 個圓盤的河內塔移動步驟"
    },
    3: {  # 圖形輸出
        1: "【聖誕樹】用 * 符號印出高度為 10 的聖誕樹（三角形加樹幹）",
        2: "【菱形】用 * 符號印出寬度為 9 的菱形",
        3: "【空心方形】用 * 符號印出邊長為 8 的空心方形",
        4: "【數字金字塔】印出數字金字塔（1, 12, 123, 1234...共 9 行）",
        5: "【九九乘法表】印出格式整齊的九九乘法表",
        6: "【Pascal 三角形】印出巴斯卡三角形前 10 行"
    },
    4: {  # 資料處理
        1: "【成績統計】建立 10 位學生的成績列表，計算平均、最高、最低、及格人數",
        2: "【詞頻統計】統計 'to be or not to be that is the question' 每個單字出現次數",
        3: "【氣溫分析】建立一週氣溫資料，找出最熱最冷的日子並計算平均溫度",
        4: "【重複過濾】從 [1,2,2,3,3,3,4,4,4,4] 中移除重複元素",
        5: "【分組統計】將 1-20 分成奇數和偶數兩組，分別計算總和",
        6: "【成績等第】將 [85,72,90,66,58,95,43,77] 轉換成等第（A/B/C/D/F）"
    },
    5: {  # 模擬實驗
        1: "【擲硬幣】模擬擲硬幣 10000 次，統計正反面次數和機率",
        2: "【骰子統計】模擬擲 2 顆骰子 10000 次，統計每種點數和的機率",
        3: "【蒙地卡羅】用隨機投點法估算圓周率（投 100000 個點）",
        4: "【生日悖論】模擬 1000 次，驗證 23 人中至少兩人同生日的機率",
        5: "【隨機漫步】模擬 2D 隨機漫步 1000 步，計算最終距離原點的距離",
        6: "【抽獎模擬】模擬抽獎 1000 次，統計 1/100 中獎率的實際結果"
    },
    6: {  # 綜合挑戰
        1: "【密碼產生器】產生 5 組 12 位隨機密碼，包含大小寫字母、數字和符號",
        2: "【凱薩密碼】將 'HELLO WORLD' 用位移 3 加密，再解密回來",
        3: "【摩斯密碼】將 'SOS' 轉成摩斯密碼，再轉回英文驗證",
        4: "【撲克牌】模擬洗牌並抽 5 張，判斷是否為同花、順子、對子等牌型",
        5: "【數字轉換】將十進位 255 轉成二進位、八進位、十六進位",
        6: "【文字遊戲】檢查 'racecar'、'hello'、'level' 是否為回文"
    }
}

# 各組的執行結果（使用 "類別_題號" 作為 key）
# 結構: groups_data[group_id]["cat_task"] = {code, output, last_run}
groups_data = {i: {} for i in range(1, 7)}


def get_task_key(category_id, task_id):
    """產生任務的唯一 key"""
    return f"{category_id}_{task_id}"


def get_group_task_data(group_id, category_id, task_id):
    """取得指定組別的指定題目資料"""
    key = get_task_key(category_id, task_id)
    if key not in groups_data[group_id]:
        groups_data[group_id][key] = {
            "code": "",
            "output": "",
            "last_run": None
        }
    return groups_data[group_id][key]


@real_app.route("/")
def index():
    """主頁面 - 顯示六個組別的練習區"""
    return render_template(
        "index.html",
        categories=CATEGORIES,
        tasks=TASKS,
        groups_data=groups_data
    )


@real_app.route("/get_task/<int:group_id>/<int:category_id>/<int:task_id>")
def get_task(group_id, category_id, task_id):
    """取得指定組別的指定題目資料"""
    if group_id not in range(1, 7):
        return jsonify({"error": "無效的組別"}), 400
    if category_id not in TASKS:
        return jsonify({"error": "無效的類別"}), 400
    if task_id not in TASKS[category_id]:
        return jsonify({"error": "無效的題目"}), 400

    task_data = get_group_task_data(group_id, category_id, task_id)
    return jsonify({
        "task": TASKS[category_id][task_id],
        "code": task_data["code"],
        "output": task_data["output"],
        "last_run": task_data["last_run"]
    })


@real_app.route("/run/<int:group_id>/<int:category_id>/<int:task_id>", methods=["POST"])
def run_code(group_id, category_id, task_id):
    """執行指定組別的指定題目程式碼"""
    if group_id not in range(1, 7):
        return jsonify({"error": "無效的組別"}), 400

    data = request.get_json()
    code = data.get("code", "")

    task_data = get_group_task_data(group_id, category_id, task_id)
    task_data["code"] = code
    task_data["last_run"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 建立暫存檔案執行程式碼
    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as f:
            f.write(code)
            temp_file = f.name

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

    task_data["output"] = output

    return jsonify({
        "output": output,
        "last_run": task_data["last_run"]
    })


@real_app.route("/save/<int:group_id>/<int:category_id>/<int:task_id>", methods=["POST"])
def save_code(group_id, category_id, task_id):
    """儲存程式碼（不執行）"""
    if group_id not in range(1, 7):
        return jsonify({"error": "無效的組別"}), 400

    data = request.get_json()
    code = data.get("code", "")

    task_data = get_group_task_data(group_id, category_id, task_id)
    task_data["code"] = code

    return jsonify({"message": "程式碼已儲存"})


@real_app.route("/get_all_data")
def get_all_data():
    """取得所有組別的所有資料"""
    return jsonify({
        "categories": CATEGORIES,
        "tasks": TASKS,
        "groups_data": groups_data
    })


@real_app.route("/get_group_summary")
def get_group_summary():
    """取得所有組別的完成狀況摘要"""
    summary = {}
    for group_id in range(1, 7):
        summary[group_id] = {
            "completed": 0,
            "total": sum(len(tasks) for tasks in TASKS.values())
        }
        for key, data in groups_data[group_id].items():
            if data.get("last_run"):
                summary[group_id]["completed"] += 1
    return jsonify(summary)


@real_app.route("/browse")
def browse():
    """瀏覽所有組別的成果"""
    return render_template(
        "browse.html",
        categories=CATEGORIES,
        tasks=TASKS,
        groups_data=groups_data
    )


@real_app.route("/clear/<int:group_id>/<int:category_id>/<int:task_id>", methods=["POST"])
def clear_task(group_id, category_id, task_id):
    """清除指定題目的程式碼和輸出"""
    if group_id not in range(1, 7):
        return jsonify({"error": "無效的組別"}), 400

    key = get_task_key(category_id, task_id)
    if key in groups_data[group_id]:
        groups_data[group_id][key] = {
            "code": "",
            "output": "",
            "last_run": None
        }

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
