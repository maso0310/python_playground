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

# 各組的題目（每組 18 題：每個難度等級 3 題，難度平均分配）
# ★ 基礎、★★ 初級、★★★ 中級、★★★★ 中高級、★★★★★ 高級、★★★★★★ 挑戰
GROUP_TASKS = {
    1: {
        # ★ 基礎 (3題)
        1: "★【變數與輸出】宣告姓名、年齡、身高三個變數，並用 f-string 印出自我介紹",
        2: "★【四則運算】計算 123+456、789-123、12*34、100/7，並格式化輸出結果",
        3: "★【字串基礎】將 'Hello World' 轉成大寫、小寫、反轉，並計算長度",
        # ★★ 初級 (3題)
        4: "★★【判斷閏年】輸入年份判斷是否為閏年，測試 2000、2024、1900、2023 年",
        5: "★★【FizzBuzz】印出 1-30，但 3 的倍數印 Fizz、5 的倍數印 Buzz、15 的倍數印 FizzBuzz",
        6: "★★【成績等第】將成績 [85,72,90,66,58,95,43,77] 轉換成等第 A/B/C/D/F",
        # ★★★ 中級 (3題)
        7: "★★★【質數判斷】寫一個函式判斷質數，並找出 1-100 之間所有質數",
        8: "★★★【九九乘法表】印出格式整齊的九九乘法表（對齊排列）",
        9: "★★★【字典統計】統計 'to be or not to be that is the question' 每個單字出現次數",
        # ★★★★ 中高級 (3題)
        10: "★★★★【聖誕樹圖案】用 * 印出高度 10 的聖誕樹（三角形+樹幹），可自訂高度",
        11: "★★★★【最大公因數】用輾轉相除法求 48 和 18 的最大公因數，印出計算過程",
        12: "★★★★【氣溫分析】建立一週氣溫字典，找出最高最低溫及平均，用函式封裝",
        # ★★★★★ 高級 (3題)
        13: "★★★★★【費氏數列】用遞迴和迴圈兩種方式產生前 20 項，比較效能差異",
        14: "★★★★★【凱薩密碼】實作加密解密函式，將 'HELLO WORLD' 位移 3 加密再解密",
        15: "★★★★★【蒙地卡羅法】用隨機投點法估算圓周率，投 100000 點並計算誤差",
        # ★★★★★★ 挑戰 (3題)
        16: "★★★★★★【撲克牌判斷】洗牌抽 5 張，判斷牌型（同花順/四條/葫蘆/同花/順子等）",
        17: "★★★★★★【河內塔遞迴】印出 4 個圓盤的河內塔移動步驟，統計總步數",
        18: "★★★★★★【感測器類別】設計 Sensor 類別，可記錄溫濕度並計算統計值"
    },
    2: {
        # ★ 基礎 (3題)
        1: "★【型別轉換】將字串 '123' 轉成整數、'3.14' 轉成浮點數，並印出型別",
        2: "★【列表基礎】建立 1-10 的列表，印出總和、平均、最大值、最小值",
        3: "★【布林運算】用 and/or/not 運算，判斷 5>3、10==10、True and False 等",
        # ★★ 初級 (3題)
        4: "★★【猜數字提示】寫一個函式，輸入猜測值和答案，回傳「太大」「太小」或「正確」",
        5: "★★【數字金字塔】印出 9 行數字金字塔（1, 12, 123...），置中對齊",
        6: "★★【奇偶分組】將 1-20 分成奇數和偶數兩組，分別計算總和",
        # ★★★ 中級 (3題)
        7: "★★★【重複過濾】用三種方法從 [1,2,2,3,3,3,4,4,4,4] 移除重複：set、迴圈、dict",
        8: "★★★【巴斯卡三角形】印出前 10 行巴斯卡三角形，格式化對齊",
        9: "★★★【進位轉換】將 255 轉成二進位、八進位、十六進位，並手動演示轉換過程",
        # ★★★★ 中高級 (3題)
        10: "★★★★【菱形圖案】用 * 印出寬度 9 的菱形，可自訂寬度參數",
        11: "★★★★【擲硬幣模擬】模擬擲硬幣 10000 次，統計正反面次數並計算機率",
        12: "★★★★【密碼驗證器】驗證密碼是否符合：8位以上、含大小寫、含數字、含特殊符號",
        # ★★★★★ 高級 (3題)
        13: "★★★★★【二分搜尋法】電腦隨機 1-100 答案，用二分法猜測並印出每步過程",
        14: "★★★★★【質數篩法】用埃拉托斯特尼篩法找 1-100 質數，視覺化篩選過程",
        15: "★★★★★【生日悖論】模擬 1000 次驗證 23 人中有相同生日的機率約 50%",
        # ★★★★★★ 挑戰 (3題)
        16: "★★★★★★【排序動畫】產生 10 個隨機數，用氣泡排序和選擇排序，印出每輪變化",
        17: "★★★★★★【密碼產生器】產生 5 組 16 位強密碼，確保包含各類字元且不重複",
        18: "★★★★★★【作物產量類別】設計 Crop 類別，可記錄種植日期、產量，計算生長天數"
    },
    3: {
        # ★ 基礎 (3題)
        1: "★【格式化輸出】用 f-string 印出購物清單：品名、單價、數量、小計",
        2: "★【字串方法】對 'Python Programming' 使用 upper/lower/title/replace 等方法",
        3: "★【列表切片】建立 1-10 列表，取出前3個、後3個、奇數位置、偶數位置的元素",
        # ★★ 初級 (3題)
        4: "★★【BMI 計算】輸入身高體重計算 BMI，並判斷體重狀態（過輕/正常/過重/肥胖）",
        5: "★★【倒數計時】用迴圈印出 10 到 1 的倒數，最後印出「發射！」",
        6: "★★【成績統計】建立 10 位學生成績列表，計算平均、最高、最低、及格人數",
        # ★★★ 中級 (3題)
        7: "★★★【空心方形】用 * 印出邊長 8 的空心方形，可自訂邊長",
        8: "★★★【回文檢查】寫函式檢查字串是否為回文，測試 'racecar'、'hello'、'A man a plan a canal Panama'",
        9: "★★★【購物車計算】建立商品字典（含價格、數量），計算總價並套用折扣",
        # ★★★★ 中高級 (3題)
        10: "★★★★【抽獎模擬】模擬 1000 次抽獎（1/100 中獎率），統計實際中獎率",
        11: "★★★★【骰子統計】模擬擲 2 顆骰子 10000 次，統計每種點數和的機率分布",
        12: "★★★★【電話簿系統】用字典實作電話簿，支援新增、查詢、刪除、列出所有聯絡人",
        # ★★★★★ 高級 (3題)
        13: "★★★★★【摩斯密碼】實作英文與摩斯密碼的雙向轉換，測試 'SOS' 和 'HELLO'",
        14: "★★★★★【隨機漫步】模擬 2D 隨機漫步 1000 步，計算最終距離原點的位置",
        15: "★★★★★【遞迴階乘】用遞迴和迴圈兩種方式計算 10!，並加入記憶化優化",
        # ★★★★★★ 挑戰 (3題)
        16: "★★★★★★【迷宮生成】用遞迴回溯法生成 15x15 隨機迷宮並印出",
        17: "★★★★★★【灌溉排程類別】設計 IrrigationSchedule 類別，可設定時間、水量、頻率",
        18: "★★★★★★【文字直方圖】讀取一段文字，用 * 繪製字母出現頻率的水平直方圖"
    },
    4: {
        # ★ 基礎 (3題)
        1: "★【輸入輸出】讓使用者輸入名字和年齡，印出歡迎訊息（可用預設值示範）",
        2: "★【數學函式】使用 math 模組計算：sqrt(16)、pi、sin(90度)、log(100)",
        3: "★【隨機數】用 random 模組產生 5 個 1-100 的隨機數，並找出最大最小值",
        # ★★ 初級 (3題)
        4: "★★【溫度轉換】寫函式將攝氏轉華氏、華氏轉攝氏，測試 0°C、100°C、32°F、212°F",
        5: "★★【星星三角形】用迴圈印出高度 5 的直角三角形（1顆星到5顆星）",
        6: "★★【列表操作】對列表 [3,1,4,1,5,9,2,6] 進行排序、反轉、插入、刪除操作",
        # ★★★ 中級 (3題)
        7: "★★★【因數分解】寫函式找出一個數的所有因數，測試 36、100、97（質數）",
        8: "★★★【字串加密】將字串每個字元的 ASCII 碼加 1 來加密，再解密回原文",
        9: "★★★【學生成績系統】用列表儲存多位學生的成績，可新增、查詢、計算班級平均",
        # ★★★★ 中高級 (3題)
        10: "★★★★【倒三角形】用 * 印出倒三角形，從最寬處遞減到 1 顆星",
        11: "★★★★【字元統計】統計字串中大寫、小寫、數字、空格、特殊符號各有幾個",
        12: "★★★★【矩陣運算】建立兩個 3x3 矩陣，計算矩陣加法和轉置",
        # ★★★★★ 高級 (3題)
        13: "★★★★★【快速排序】實作快速排序演算法，對 [64,34,25,12,22,11,90] 排序並印出過程",
        14: "★★★★★【括號配對】寫函式檢查字串的括號是否配對正確，支援 ()[]{}",
        15: "★★★★★【LRU 快取】用字典實作簡易 LRU 快取，容量 3，測試存取順序",
        # ★★★★★★ 挑戰 (3題)
        16: "★★★★★★【八皇后問題】用回溯法找出 8x8 棋盤上放置 8 個皇后的一種解法",
        17: "★★★★★★【溫室控制類別】設計 Greenhouse 類別，可監控溫濕度、自動調節、發出警報",
        18: "★★★★★★【表達式計算機】實作可計算含括號的四則運算字串，如 '(3+4)*2'"
    },
    5: {
        # ★ 基礎 (3題)
        1: "★【字典建立】建立學生資料字典（姓名、學號、成績），印出各項資訊",
        2: "★【集合操作】建立兩個集合 {1,2,3,4} 和 {3,4,5,6}，印出聯集、交集、差集",
        3: "★【元組操作】建立座標元組 (3, 4)，計算距離原點的距離",
        # ★★ 初級 (3題)
        4: "★★【日期計算】輸入生日，計算年齡（用 datetime 模組）",
        5: "★★【字母統計】統計 'Hello, World!' 中每個字母（忽略大小寫）出現的次數",
        6: "★★【數字反轉】輸入一個正整數，印出其反轉結果（如 12345 → 54321）",
        # ★★★ 中級 (3題)
        7: "★★★【完美數檢查】寫函式判斷完美數（因數和等於自身），找出 1-1000 的完美數",
        8: "★★★【字串壓縮】將 'AAABBBCCDDDD' 壓縮成 'A3B3C2D4'，並可解壓縮回原字串",
        9: "★★★【庫存管理】用字典管理商品庫存，支援進貨、出貨、查詢、低庫存警告",
        # ★★★★ 中高級 (3題)
        10: "★★★★【螺旋矩陣】生成 5x5 的螺旋矩陣（從外到內填入 1-25）",
        11: "★★★★【質因數分解】將一個數分解為質因數的乘積，如 60 = 2×2×3×5",
        12: "★★★★【井字遊戲棋盤】用 2D 列表建立井字遊戲棋盤，可放置 X/O 並判斷勝負",
        # ★★★★★ 高級 (3題)
        13: "★★★★★【合併排序】實作合併排序演算法，印出分割和合併的過程",
        14: "★★★★★【最長共同子序列】找出兩字串 'ABCDGH' 和 'AEDFHR' 的最長共同子序列",
        15: "★★★★★【裝飾器計時】寫一個裝飾器函式，可計算任意函式的執行時間",
        # ★★★★★★ 挑戰 (3題)
        16: "★★★★★★【數獨驗證器】寫函式驗證一個完成的 9x9 數獨是否合法",
        17: "★★★★★★【農場動物類別】設計 Animal 基類和 Cow/Chicken/Pig 子類，實作多型",
        18: "★★★★★★【路徑搜尋 BFS】用 BFS 找出迷宮從起點到終點的最短路徑"
    },
    6: {
        # ★ 基礎 (3題)
        1: "★【迴圈練習】用 for 迴圈印出 1-100 中所有 3 或 5 的倍數",
        2: "★【字串格式化】用三種方式格式化：% 運算子、format()、f-string，印出相同結果",
        3: "★【列表生成式】用列表生成式產生 1-10 的平方數 [1,4,9,...,100]",
        # ★★ 初級 (3題)
        4: "★★【質數檢查】寫一個函式判斷單一數字是否為質數，測試多個數字",
        5: "★★【字串處理】移除字串中的所有空格和標點符號，只保留字母和數字",
        6: "★★【階乘計算】用迴圈和遞迴兩種方式計算 10 的階乘",
        # ★★★ 中級 (3題)
        7: "★★★【二進位轉換】手動實作十進位轉二進位，印出轉換過程（不用 bin 函式）",
        8: "★★★【沙漏圖案】用 * 印出沙漏形狀（上半倒三角+下半正三角）",
        9: "★★★【成績管理字典】用巢狀字典管理多班級多學生成績，可查詢班級/個人平均",
        # ★★★★ 中高級 (3題)
        10: "★★★★【矩陣乘法】實作 2x3 和 3x2 矩陣相乘，得到 2x2 結果矩陣",
        11: "★★★★【最小公倍數】用最大公因數計算最小公倍數，求 12、18、24 的最小公倍數",
        12: "★★★★【文字藝術字】將輸入文字轉成大型 ASCII 藝術字（至少支援數字 0-9）",
        # ★★★★★ 高級 (3題)
        13: "★★★★★【堆疊計算機】用堆疊實作後序表達式計算，如 '3 4 + 2 *' = 14",
        14: "★★★★★【生成器函式】用 yield 寫一個無限費氏數列生成器，取前 20 項",
        15: "★★★★★【圖形走訪 DFS】用 DFS 走訪圖形，找出從節點 A 到 F 的所有路徑",
        # ★★★★★★ 挑戰 (3題)
        16: "★★★★★★【貪婪演算法】用貪婪法解決找零問題：用最少硬幣湊出指定金額",
        17: "★★★★★★【感測網路類別】設計 SensorNetwork 類別，可新增感測器、聚合資料、偵測異常",
        18: "★★★★★★【Dijkstra 最短路徑】實作 Dijkstra 演算法，找出加權圖中兩點最短路徑"
    }
}

# 各組的執行結果
# 結構: groups_data[group_id][task_id] = {code, output, last_run}
groups_data = {i: {} for i in range(1, 7)}

# ============================================================
# 從 answers 模組載入預設答案（展示用，可刪除）
# ============================================================
try:
    from answers import ALL_ANSWERS
    SAMPLE_ANSWERS = ALL_ANSWERS
except ImportError:
    SAMPLE_ANSWERS = {}


def init_sample_data():
    """初始化範例答案資料"""
    for group_id, tasks in SAMPLE_ANSWERS.items():
        for task_id, data in tasks.items():
            groups_data[group_id][task_id] = {
                "code": data["code"],
                "output": data["output"],
                "last_run": "2024-12-28 10:00:00"
            }


# 啟動時載入範例資料（展示用，可刪除此行）
init_sample_data()


def get_group_task_data(group_id, task_id):
    """取得指定組別的指定題目資料"""
    if task_id not in groups_data[group_id]:
        groups_data[group_id][task_id] = {
            "code": "",
            "output": "",
            "last_run": None
        }
    return groups_data[group_id][task_id]


@real_app.route("/")
def index():
    """主頁面 - 顯示六個組別的練習區"""
    return render_template(
        "index.html",
        group_tasks=GROUP_TASKS,
        groups_data=groups_data
    )


@real_app.route("/get_task/<int:group_id>/<int:task_id>")
def get_task(group_id, task_id):
    """取得指定組別的指定題目資料"""
    if group_id not in range(1, 7):
        return jsonify({"error": "無效的組別"}), 400
    if task_id not in GROUP_TASKS[group_id]:
        return jsonify({"error": "無效的題目"}), 400

    task_data = get_group_task_data(group_id, task_id)
    return jsonify({
        "task": GROUP_TASKS[group_id][task_id],
        "code": task_data["code"],
        "output": task_data["output"],
        "last_run": task_data["last_run"]
    })


@real_app.route("/run/<int:group_id>/<int:task_id>", methods=["POST"])
def run_code(group_id, task_id):
    """執行指定組別的指定題目程式碼"""
    if group_id not in range(1, 7):
        return jsonify({"error": "無效的組別"}), 400

    data = request.get_json()
    code = data.get("code", "")

    task_data = get_group_task_data(group_id, task_id)
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


@real_app.route("/save/<int:group_id>/<int:task_id>", methods=["POST"])
def save_code(group_id, task_id):
    """儲存程式碼（不執行）"""
    if group_id not in range(1, 7):
        return jsonify({"error": "無效的組別"}), 400

    data = request.get_json()
    code = data.get("code", "")

    task_data = get_group_task_data(group_id, task_id)
    task_data["code"] = code

    return jsonify({"message": "程式碼已儲存"})


@real_app.route("/get_all_data")
def get_all_data():
    """取得所有組別的所有資料"""
    return jsonify({
        "group_tasks": GROUP_TASKS,
        "groups_data": groups_data
    })


@real_app.route("/get_group_summary")
def get_group_summary():
    """取得所有組別的完成狀況摘要"""
    summary = {}
    for group_id in range(1, 7):
        summary[group_id] = {
            "completed": 0,
            "total": 18  # 每組固定 18 題
        }
        for task_id, data in groups_data[group_id].items():
            if data.get("last_run"):
                summary[group_id]["completed"] += 1
    return jsonify(summary)


@real_app.route("/browse")
def browse():
    """瀏覽所有組別的成果"""
    return render_template(
        "browse.html",
        group_tasks=GROUP_TASKS,
        groups_data=groups_data
    )


@real_app.route("/clear/<int:group_id>/<int:task_id>", methods=["POST"])
def clear_task(group_id, task_id):
    """清除指定題目的程式碼和輸出"""
    if group_id not in range(1, 7):
        return jsonify({"error": "無效的組別"}), 400

    if task_id in groups_data[group_id]:
        groups_data[group_id][task_id] = {
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
