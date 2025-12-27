"""
Python Playground - 36 題參考答案
智慧農業課程

每組 6 題，共 6 組 = 36 題
"""

# ============================================================
# 第 1 組：基礎練習
# ============================================================

# --- 題目 1：變數練習 ---
# 宣告姓名、年齡、身高三個變數，並印出自我介紹
def group1_task1():
    name = "小明"
    age = 18
    height = 170.5

    print(f"大家好，我是{name}")
    print(f"我今年 {age} 歲")
    print(f"我的身高是 {height} 公分")
    print(f"很高興認識大家！")

# --- 題目 2：計算機 ---
# 計算 123 + 456、789 - 123、12 * 34、100 / 7 的結果
def group1_task2():
    print(f"123 + 456 = {123 + 456}")
    print(f"789 - 123 = {789 - 123}")
    print(f"12 * 34 = {12 * 34}")
    print(f"100 / 7 = {100 / 7:.4f}")

# --- 題目 3：字串操作 ---
# 將 'Hello World' 轉成大寫、小寫、反轉，並計算長度
def group1_task3():
    text = "Hello World"

    print(f"原始字串: {text}")
    print(f"轉大寫: {text.upper()}")
    print(f"轉小寫: {text.lower()}")
    print(f"反轉: {text[::-1]}")
    print(f"長度: {len(text)}")

# --- 題目 4：列表操作 ---
# 建立 1-10 的列表，印出總和、平均、最大、最小值
def group1_task4():
    numbers = list(range(1, 11))

    print(f"列表: {numbers}")
    print(f"總和: {sum(numbers)}")
    print(f"平均: {sum(numbers) / len(numbers)}")
    print(f"最大值: {max(numbers)}")
    print(f"最小值: {min(numbers)}")

# --- 題目 5：字典練習 ---
# 建立一個學生資料字典（姓名、學號、成績），並印出內容
def group1_task5():
    student = {
        "姓名": "王小明",
        "學號": "A12345678",
        "成績": {
            "國文": 85,
            "英文": 92,
            "數學": 78
        }
    }

    print("=== 學生資料 ===")
    print(f"姓名: {student['姓名']}")
    print(f"學號: {student['學號']}")
    print("成績:")
    for subject, score in student['成績'].items():
        print(f"  {subject}: {score} 分")

# --- 題目 6：迴圈練習 ---
# 用 for 迴圈印出 1-100 中所有 3 的倍數
def group1_task6():
    print("1-100 中所有 3 的倍數:")
    multiples = []
    for i in range(1, 101):
        if i % 3 == 0:
            multiples.append(i)

    print(multiples)
    print(f"共有 {len(multiples)} 個")


# ============================================================
# 第 2 組：演算法
# ============================================================

# --- 題目 1：二分搜尋 ---
# 電腦隨機產生 1-100 的答案，用二分法自動猜測並印出過程
def group2_task1():
    import random

    answer = random.randint(1, 100)
    print(f"答案是: {answer}")
    print("=" * 30)
    print("開始用二分法猜測:")

    low, high = 1, 100
    count = 0

    while low <= high:
        count += 1
        guess = (low + high) // 2
        print(f"第 {count} 次猜測: {guess} (範圍: {low}-{high})")

        if guess == answer:
            print(f"猜對了！答案是 {answer}，共猜了 {count} 次")
            break
        elif guess < answer:
            print(f"  {guess} 太小了")
            low = guess + 1
        else:
            print(f"  {guess} 太大了")
            high = guess - 1

# --- 題目 2：排序比較 ---
# 產生 10 個隨機數字，分別用氣泡排序和選擇排序印出過程
def group2_task2():
    import random

    # 產生隨機數字
    original = [random.randint(1, 100) for _ in range(10)]
    print(f"原始數列: {original}")
    print()

    # 氣泡排序
    print("=== 氣泡排序 ===")
    arr = original.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"第 {i+1} 輪: {arr}")

    print()

    # 選擇排序
    print("=== 選擇排序 ===")
    arr = original.copy()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"第 {i+1} 輪: {arr}")

# --- 題目 3：費氏數列 ---
# 印出費氏數列前 20 項，並計算第 20 項的值
def group2_task3():
    fib = [0, 1]
    for i in range(2, 20):
        fib.append(fib[i-1] + fib[i-2])

    print("費氏數列前 20 項:")
    for i, num in enumerate(fib, 1):
        print(f"第 {i:2d} 項: {num}")

    print(f"\n第 20 項的值是: {fib[19]}")

# --- 題目 4：質數篩選 ---
# 找出 1-100 之間所有的質數
def group2_task4():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [n for n in range(1, 101) if is_prime(n)]

    print("1-100 之間的質數:")
    print(primes)
    print(f"\n共有 {len(primes)} 個質數")

# --- 題目 5：最大公因數 ---
# 實作輾轉相除法，計算 48 和 18 的最大公因數
def group2_task5():
    def gcd(a, b):
        print(f"計算 GCD({a}, {b})")
        while b != 0:
            print(f"  {a} = {b} × {a // b} + {a % b}")
            a, b = b, a % b
        return a

    num1, num2 = 48, 18
    result = gcd(num1, num2)
    print(f"\n{num1} 和 {num2} 的最大公因數是: {result}")

# --- 題目 6：河內塔 ---
# 印出 4 個圓盤的河內塔移動步驟
def group2_task6():
    def hanoi(n, source, target, auxiliary, step=[0]):
        if n == 1:
            step[0] += 1
            print(f"步驟 {step[0]:2d}: 將圓盤 1 從 {source} 移到 {target}")
            return
        hanoi(n-1, source, auxiliary, target, step)
        step[0] += 1
        print(f"步驟 {step[0]:2d}: 將圓盤 {n} 從 {source} 移到 {target}")
        hanoi(n-1, auxiliary, target, source, step)

    print("河內塔 - 4 個圓盤的移動步驟:")
    print("(A: 起始柱, B: 輔助柱, C: 目標柱)")
    print("=" * 40)
    hanoi(4, 'A', 'C', 'B')
    print(f"\n總共需要 {2**4 - 1} 步")


# ============================================================
# 第 3 組：圖形輸出
# ============================================================

# --- 題目 1：聖誕樹 ---
# 用 * 符號印出高度為 10 的聖誕樹（三角形加樹幹）
def group3_task1():
    height = 10

    # 印出三角形樹冠
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    # 印出樹幹
    trunk_width = 3
    trunk_height = 2
    for _ in range(trunk_height):
        spaces = " " * (height - trunk_width // 2 - 1)
        trunk = "*" * trunk_width
        print(spaces + trunk)

# --- 題目 2：菱形 ---
# 用 * 符號印出寬度為 9 的菱形
def group3_task2():
    width = 9
    mid = width // 2 + 1

    # 上半部（含中間）
    for i in range(1, mid + 1):
        spaces = " " * (mid - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    # 下半部
    for i in range(mid - 1, 0, -1):
        spaces = " " * (mid - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# --- 題目 3：空心方形 ---
# 用 * 符號印出邊長為 8 的空心方形
def group3_task3():
    size = 8

    for i in range(size):
        for j in range(size):
            if i == 0 or i == size-1 or j == 0 or j == size-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# --- 題目 4：數字金字塔 ---
# 印出數字金字塔（1, 12, 123, 1234...共 9 行）
def group3_task4():
    rows = 9

    for i in range(1, rows + 1):
        # 印出前導空格
        spaces = " " * (rows - i)
        # 印出數字
        numbers = "".join(str(j) for j in range(1, i + 1))
        print(spaces + numbers)

# --- 題目 5：九九乘法表 ---
# 印出格式整齊的九九乘法表
def group3_task5():
    print("=== 九九乘法表 ===")
    print()

    # 印出表頭
    print("    ", end="")
    for i in range(1, 10):
        print(f"{i:4d}", end="")
    print()
    print("    " + "-" * 36)

    # 印出乘法表
    for i in range(1, 10):
        print(f"{i:2d} |", end="")
        for j in range(1, 10):
            print(f"{i*j:4d}", end="")
        print()

# --- 題目 6：Pascal 三角形 ---
# 印出巴斯卡三角形前 10 行
def group3_task6():
    rows = 10
    triangle = []

    for i in range(rows):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)

    print("巴斯卡三角形前 10 行:")
    print()

    # 格式化輸出
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))


# ============================================================
# 第 4 組：資料處理
# ============================================================

# --- 題目 1：成績統計 ---
# 建立 10 位學生的成績列表，計算平均、最高、最低、及格人數
def group4_task1():
    scores = [85, 72, 90, 66, 58, 95, 43, 77, 88, 61]

    print(f"學生成績: {scores}")
    print(f"平均分數: {sum(scores) / len(scores):.1f}")
    print(f"最高分: {max(scores)}")
    print(f"最低分: {min(scores)}")

    passing = [s for s in scores if s >= 60]
    print(f"及格人數: {len(passing)} 人")
    print(f"不及格人數: {len(scores) - len(passing)} 人")

# --- 題目 2：詞頻統計 ---
# 統計 'to be or not to be that is the question' 每個單字出現次數
def group4_task2():
    text = "to be or not to be that is the question"
    words = text.split()

    # 方法一：用字典
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print(f"原文: {text}")
    print(f"\n詞頻統計:")
    for word, count in sorted(word_count.items(), key=lambda x: -x[1]):
        print(f"  {word}: {count} 次")

# --- 題目 3：氣溫分析 ---
# 建立一週氣溫資料，找出最熱最冷的日子並計算平均溫度
def group4_task3():
    days = ["週一", "週二", "週三", "週四", "週五", "週六", "週日"]
    temps = [28, 30, 32, 29, 27, 31, 33]

    weather = dict(zip(days, temps))

    print("=== 一週氣溫資料 ===")
    for day, temp in weather.items():
        print(f"{day}: {temp}°C")

    max_temp = max(temps)
    min_temp = min(temps)
    avg_temp = sum(temps) / len(temps)

    hottest = days[temps.index(max_temp)]
    coldest = days[temps.index(min_temp)]

    print(f"\n最熱的日子: {hottest} ({max_temp}°C)")
    print(f"最冷的日子: {coldest} ({min_temp}°C)")
    print(f"平均溫度: {avg_temp:.1f}°C")

# --- 題目 4：重複過濾 ---
# 從 [1,2,2,3,3,3,4,4,4,4] 中移除重複元素
def group4_task4():
    original = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

    print(f"原始列表: {original}")

    # 方法一：使用 set
    unique_set = list(set(original))
    print(f"方法一 (set): {sorted(unique_set)}")

    # 方法二：保持順序
    unique_ordered = []
    for item in original:
        if item not in unique_ordered:
            unique_ordered.append(item)
    print(f"方法二 (保持順序): {unique_ordered}")

    # 方法三：使用 dict.fromkeys()
    unique_dict = list(dict.fromkeys(original))
    print(f"方法三 (dict): {unique_dict}")

# --- 題目 5：分組統計 ---
# 將 1-20 分成奇數和偶數兩組，分別計算總和
def group4_task5():
    numbers = list(range(1, 21))

    odd = [n for n in numbers if n % 2 == 1]
    even = [n for n in numbers if n % 2 == 0]

    print(f"1-20 的數字: {numbers}")
    print()
    print(f"奇數: {odd}")
    print(f"奇數總和: {sum(odd)}")
    print()
    print(f"偶數: {even}")
    print(f"偶數總和: {sum(even)}")

# --- 題目 6：成績等第 ---
# 將 [85,72,90,66,58,95,43,77] 轉換成等第（A/B/C/D/F）
def group4_task6():
    scores = [85, 72, 90, 66, 58, 95, 43, 77]

    def get_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

    print("成績等第轉換:")
    print("-" * 20)

    for score in scores:
        grade = get_grade(score)
        print(f"{score} 分 → {grade}")

    # 統計各等第人數
    grades = [get_grade(s) for s in scores]
    print("\n等第分布:")
    for g in ['A', 'B', 'C', 'D', 'F']:
        count = grades.count(g)
        print(f"  {g}: {count} 人")


# ============================================================
# 第 5 組：模擬實驗
# ============================================================

# --- 題目 1：擲硬幣 ---
# 模擬擲硬幣 10000 次，統計正反面次數和機率
def group5_task1():
    import random

    trials = 10000
    heads = 0
    tails = 0

    for _ in range(trials):
        if random.choice(['正面', '反面']) == '正面':
            heads += 1
        else:
            tails += 1

    print(f"擲硬幣 {trials} 次的結果:")
    print(f"正面: {heads} 次 ({heads/trials*100:.2f}%)")
    print(f"反面: {tails} 次 ({tails/trials*100:.2f}%)")

# --- 題目 2：骰子統計 ---
# 模擬擲 2 顆骰子 10000 次，統計每種點數和的機率
def group5_task2():
    import random

    trials = 10000
    results = {i: 0 for i in range(2, 13)}

    for _ in range(trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        results[total] += 1

    print(f"擲 2 顆骰子 {trials} 次的點數和分布:")
    print("-" * 35)

    for total, count in results.items():
        prob = count / trials * 100
        bar = "█" * int(prob * 2)
        print(f"點數和 {total:2d}: {count:4d} 次 ({prob:5.2f}%) {bar}")

# --- 題目 3：蒙地卡羅 ---
# 用隨機投點法估算圓周率（投 100000 個點）
def group5_task3():
    import random

    total_points = 100000
    inside_circle = 0

    for _ in range(total_points):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / total_points

    print("=== 蒙地卡羅法估算圓周率 ===")
    print(f"投點數量: {total_points}")
    print(f"落在圓內的點: {inside_circle}")
    print(f"估算的圓周率: {pi_estimate:.6f}")
    print(f"實際圓周率: 3.141593")
    print(f"誤差: {abs(pi_estimate - 3.141593):.6f}")

# --- 題目 4：生日悖論 ---
# 模擬 1000 次，驗證 23 人中至少兩人同生日的機率
def group5_task4():
    import random

    simulations = 1000
    people = 23
    matches = 0

    for _ in range(simulations):
        birthdays = [random.randint(1, 365) for _ in range(people)]
        if len(birthdays) != len(set(birthdays)):
            matches += 1

    probability = matches / simulations * 100

    print("=== 生日悖論模擬 ===")
    print(f"模擬次數: {simulations}")
    print(f"人數: {people} 人")
    print(f"有重複生日的次數: {matches}")
    print(f"實驗機率: {probability:.1f}%")
    print(f"理論機率: 約 50.7%")

# --- 題目 5：隨機漫步 ---
# 模擬 2D 隨機漫步 1000 步，計算最終距離原點的距離
def group5_task5():
    import random
    import math

    steps = 1000
    x, y = 0, 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for _ in range(steps):
        dx, dy = random.choice(directions)
        x += dx
        y += dy

    distance = math.sqrt(x*x + y*y)

    print("=== 2D 隨機漫步 ===")
    print(f"步數: {steps}")
    print(f"最終位置: ({x}, {y})")
    print(f"距離原點: {distance:.2f}")
    print(f"理論期望距離: {math.sqrt(steps):.2f}")

# --- 題目 6：抽獎模擬 ---
# 模擬抽獎 1000 次，統計 1/100 中獎率的實際結果
def group5_task6():
    import random

    trials = 1000
    win_rate = 1/100
    wins = 0

    for _ in range(trials):
        if random.random() < win_rate:
            wins += 1

    actual_rate = wins / trials * 100
    expected = trials * win_rate

    print("=== 抽獎模擬 ===")
    print(f"抽獎次數: {trials}")
    print(f"設定中獎率: {win_rate*100}%")
    print(f"中獎次數: {wins}")
    print(f"實際中獎率: {actual_rate:.1f}%")
    print(f"期望中獎次數: {expected:.0f}")


# ============================================================
# 第 6 組：綜合挑戰
# ============================================================

# --- 題目 1：密碼產生器 ---
# 產生 5 組 12 位隨機密碼，包含大小寫字母、數字和符號
def group6_task1():
    import random
    import string

    def generate_password(length=12):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(chars) for _ in range(length))
        return password

    print("=== 隨機密碼產生器 ===")
    print("產生 5 組 12 位密碼:\n")

    for i in range(1, 6):
        pwd = generate_password(12)
        print(f"密碼 {i}: {pwd}")

# --- 題目 2：凱薩密碼 ---
# 將 'HELLO WORLD' 用位移 3 加密，再解密回來
def group6_task2():
    def caesar_cipher(text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        return result

    original = "HELLO WORLD"
    shift = 3

    encrypted = caesar_cipher(original, shift)
    decrypted = caesar_cipher(encrypted, -shift)

    print("=== 凱薩密碼 ===")
    print(f"原文: {original}")
    print(f"位移: {shift}")
    print(f"加密後: {encrypted}")
    print(f"解密後: {decrypted}")

# --- 題目 3：摩斯密碼 ---
# 將 'SOS' 轉成摩斯密碼，再轉回英文驗證
def group6_task3():
    MORSE_CODE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..'
    }

    REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}

    def to_morse(text):
        return ' '.join(MORSE_CODE.get(c, '') for c in text.upper())

    def from_morse(morse):
        return ''.join(REVERSE_MORSE.get(c, '') for c in morse.split())

    original = "SOS"
    morse = to_morse(original)
    decoded = from_morse(morse)

    print("=== 摩斯密碼 ===")
    print(f"原文: {original}")
    print(f"摩斯密碼: {morse}")
    print(f"解碼後: {decoded}")
    print(f"驗證: {'成功' if original == decoded else '失敗'}")

# --- 題目 4：撲克牌 ---
# 模擬洗牌並抽 5 張，判斷是否為同花、順子、對子等牌型
def group6_task4():
    import random

    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    # 建立牌組
    deck = [(rank, suit) for suit in suits for rank in ranks]

    # 洗牌
    random.shuffle(deck)

    # 抽 5 張
    hand = deck[:5]

    print("=== 撲克牌判斷 ===")
    print(f"抽到的牌: {[f'{r}{s}' for r, s in hand]}")
    print()

    # 分析牌型
    hand_suits = [s for r, s in hand]
    hand_ranks = [r for r, s in hand]

    # 判斷同花
    is_flush = len(set(hand_suits)) == 1

    # 判斷順子
    rank_values = []
    for r in hand_ranks:
        if r == 'A':
            rank_values.append(1)
        elif r == 'J':
            rank_values.append(11)
        elif r == 'Q':
            rank_values.append(12)
        elif r == 'K':
            rank_values.append(13)
        else:
            rank_values.append(int(r))

    rank_values.sort()
    is_straight = (rank_values == list(range(rank_values[0], rank_values[0]+5)))

    # 判斷對子、三條、四條
    rank_count = {}
    for r in hand_ranks:
        rank_count[r] = rank_count.get(r, 0) + 1

    counts = sorted(rank_count.values(), reverse=True)

    # 判斷牌型
    if is_flush and is_straight:
        hand_type = "同花順"
    elif counts[0] == 4:
        hand_type = "四條"
    elif counts[0] == 3 and counts[1] == 2:
        hand_type = "葫蘆"
    elif is_flush:
        hand_type = "同花"
    elif is_straight:
        hand_type = "順子"
    elif counts[0] == 3:
        hand_type = "三條"
    elif counts[0] == 2 and counts[1] == 2:
        hand_type = "兩對"
    elif counts[0] == 2:
        hand_type = "一對"
    else:
        hand_type = "散牌"

    print(f"牌型: {hand_type}")

# --- 題目 5：數字轉換 ---
# 將十進位 255 轉成二進位、八進位、十六進位
def group6_task5():
    decimal = 255

    print("=== 進位轉換 ===")
    print(f"十進位: {decimal}")
    print(f"二進位: {bin(decimal)} = {bin(decimal)[2:]}")
    print(f"八進位: {oct(decimal)} = {oct(decimal)[2:]}")
    print(f"十六進位: {hex(decimal)} = {hex(decimal)[2:].upper()}")

    # 手動轉換二進位
    print("\n手動轉換二進位過程:")
    n = decimal
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        print(f"  {n} ÷ 2 = {n//2} ... {n%2}")
        n //= 2
    print(f"結果: {binary}")

# --- 題目 6：文字遊戲 ---
# 檢查 'racecar'、'hello'、'level' 是否為回文
def group6_task6():
    def is_palindrome(s):
        s = s.lower()
        return s == s[::-1]

    words = ['racecar', 'hello', 'level']

    print("=== 回文檢查 ===")
    for word in words:
        reversed_word = word[::-1]
        result = "是回文" if is_palindrome(word) else "不是回文"
        print(f"'{word}' 反轉後是 '{reversed_word}' → {result}")


# ============================================================
# 主程式 - 執行所有題目
# ============================================================

if __name__ == "__main__":
    # 定義所有題目函數
    all_tasks = {
        1: [group1_task1, group1_task2, group1_task3, group1_task4, group1_task5, group1_task6],
        2: [group2_task1, group2_task2, group2_task3, group2_task4, group2_task5, group2_task6],
        3: [group3_task1, group3_task2, group3_task3, group3_task4, group3_task5, group3_task6],
        4: [group4_task1, group4_task2, group4_task3, group4_task4, group4_task5, group4_task6],
        5: [group5_task1, group5_task2, group5_task3, group5_task4, group5_task5, group5_task6],
        6: [group6_task1, group6_task2, group6_task3, group6_task4, group6_task5, group6_task6],
    }

    group_names = {
        1: "基礎練習", 2: "演算法", 3: "圖形輸出",
        4: "資料處理", 5: "模擬實驗", 6: "綜合挑戰"
    }

    print("=" * 60)
    print("Python Playground - 36 題參考答案")
    print("=" * 60)

    for group_id, tasks in all_tasks.items():
        print(f"\n{'='*60}")
        print(f"第 {group_id} 組：{group_names[group_id]}")
        print(f"{'='*60}")

        for task_id, task_func in enumerate(tasks, 1):
            print(f"\n--- 題目 {task_id} ---")
            try:
                task_func()
            except Exception as e:
                print(f"執行錯誤: {e}")
            print()
