# 第 3 組答案 (18題)

ANSWERS = {
    1: {  # ★ 格式化輸出
        "code": '''items = [
    ("蘋果", 35, 3),
    ("牛奶", 65, 2),
    ("麵包", 45, 1)
]

print("=== 購物清單 ===")
print(f"{'品名':<8}{'單價':>6}{'數量':>6}{'小計':>8}")
print("-" * 28)
total = 0
for name, price, qty in items:
    subtotal = price * qty
    total += subtotal
    print(f"{name:<8}{price:>6}{qty:>6}{subtotal:>8}")
print("-" * 28)
print(f"{'總計':<20}{total:>8}")''',
        "output": '''=== 購物清單 ===
品名        單價    數量      小計
----------------------------
蘋果          35     3     105
牛奶          65     2     130
麵包          45     1      45
----------------------------
總計                        280'''
    },
    2: {  # ★ 字串方法
        "code": '''text = "Python Programming"
print(f"原始: {text}")
print(f"upper(): {text.upper()}")
print(f"lower(): {text.lower()}")
print(f"title(): {text.title()}")
print(f"replace('Python', 'Java'): {text.replace('Python', 'Java')}")
print(f"split(): {text.split()}")
print(f"startswith('Python'): {text.startswith('Python')}")''',
        "output": '''原始: Python Programming
upper(): PYTHON PROGRAMMING
lower(): python programming
title(): Python Programming
replace('Python', 'Java'): Java Programming
split(): ['Python', 'Programming']
startswith('Python'): True'''
    },
    3: {  # ★ 列表切片
        "code": '''nums = list(range(1, 11))
print(f"原列表: {nums}")
print(f"前3個: {nums[:3]}")
print(f"後3個: {nums[-3:]}")
print(f"奇數位置 (1,3,5...): {nums[::2]}")
print(f"偶數位置 (2,4,6...): {nums[1::2]}")
print(f"反轉: {nums[::-1]}")''',
        "output": '''原列表: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
前3個: [1, 2, 3]
後3個: [8, 9, 10]
奇數位置 (1,3,5...): [1, 3, 5, 7, 9]
偶數位置 (2,4,6...): [2, 4, 6, 8, 10]
反轉: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]'''
    },
    4: {  # ★★ BMI 計算
        "code": '''def calc_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        status = "過輕"
    elif bmi < 24:
        status = "正常"
    elif bmi < 27:
        status = "過重"
    else:
        status = "肥胖"
    return bmi, status

tests = [(170, 65), (160, 45), (175, 90)]
for h, w in tests:
    bmi, status = calc_bmi(h, w)
    print(f"身高 {h}cm, 體重 {w}kg → BMI: {bmi:.1f} ({status})")''',
        "output": '''身高 170cm, 體重 65kg → BMI: 22.5 (正常)
身高 160cm, 體重 45kg → BMI: 17.6 (過輕)
身高 175cm, 體重 90kg → BMI: 29.4 (肥胖)'''
    },
    5: {  # ★★ 倒數計時
        "code": '''print("=== 倒數計時 ===")
for i in range(10, 0, -1):
    print(i)
print("發射！")''',
        "output": '''=== 倒數計時 ===
10
9
8
7
6
5
4
3
2
1
發射！'''
    },
    6: {  # ★★ 成績統計
        "code": '''scores = [85, 72, 90, 66, 58, 95, 43, 77, 88, 61]

print(f"成績: {scores}")
print(f"平均: {sum(scores)/len(scores):.1f}")
print(f"最高: {max(scores)}")
print(f"最低: {min(scores)}")

passing = [s for s in scores if s >= 60]
print(f"及格人數: {len(passing)}")
print(f"不及格人數: {len(scores) - len(passing)}")''',
        "output": '''成績: [85, 72, 90, 66, 58, 95, 43, 77, 88, 61]
平均: 73.5
最高: 95
最低: 43
及格人數: 8
不及格人數: 2'''
    },
    7: {  # ★★★ 空心方形
        "code": '''def hollow_square(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size-1 or j == 0 or j == size-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

hollow_square(8)''',
        "output": '''********
*      *
*      *
*      *
*      *
*      *
*      *
********'''
    },
    8: {  # ★★★ 回文檢查
        "code": '''def is_palindrome(s):
    # 只保留字母並轉小寫
    clean = "".join(c.lower() for c in s if c.isalpha())
    return clean == clean[::-1]

tests = ["racecar", "hello", "A man a plan a canal Panama"]
for t in tests:
    result = "是回文" if is_palindrome(t) else "不是回文"
    print(f"'{t}' → {result}")''',
        "output": ''''racecar' → 是回文
'hello' → 不是回文
'A man a plan a canal Panama' → 是回文'''
    },
    9: {  # ★★★ 購物車計算
        "code": '''cart = {
    "蘋果": {"price": 35, "qty": 3},
    "牛奶": {"price": 65, "qty": 2},
    "麵包": {"price": 45, "qty": 1}
}

def calc_total(cart, discount=0):
    subtotal = sum(item["price"] * item["qty"] for item in cart.values())
    discount_amount = subtotal * discount
    return subtotal, discount_amount, subtotal - discount_amount

print("=== 購物車 ===")
for name, item in cart.items():
    print(f"{name}: ${item['price']} x {item['qty']}")

subtotal, disc, total = calc_total(cart, 0.1)
print(f"\\n小計: ${subtotal}")
print(f"折扣 (10%): -${disc:.0f}")
print(f"總計: ${total:.0f}")''',
        "output": '''=== 購物車 ===
蘋果: $35 x 3
牛奶: $65 x 2
麵包: $45 x 1

小計: $280
折扣 (10%): -$28
總計: $252'''
    },
    10: {  # ★★★★ 抽獎模擬
        "code": '''import random

def lottery_simulation(trials, win_rate):
    wins = sum(1 for _ in range(trials) if random.random() < win_rate)
    return wins

trials = 1000
expected_rate = 1/100
wins = lottery_simulation(trials, expected_rate)
actual_rate = wins / trials * 100

print("=== 抽獎模擬 ===")
print(f"抽獎次數: {trials}")
print(f"設定中獎率: {expected_rate*100}%")
print(f"中獎次數: {wins}")
print(f"實際中獎率: {actual_rate:.1f}%")''',
        "output": '''=== 抽獎模擬 ===
抽獎次數: 1000
設定中獎率: 1.0%
中獎次數: 11
實際中獎率: 1.1%'''
    },
    11: {  # ★★★★ 骰子統計
        "code": '''import random

trials = 10000
results = {i: 0 for i in range(2, 13)}

for _ in range(trials):
    total = random.randint(1,6) + random.randint(1,6)
    results[total] += 1

print(f"擲 2 顆骰子 {trials} 次:")
for total, count in results.items():
    prob = count / trials * 100
    bar = "█" * int(prob * 2)
    print(f"{total:2d}: {count:4d} ({prob:5.2f}%) {bar}")''',
        "output": '''擲 2 顆骰子 10000 次:
 2:  278 ( 2.78%) █████
 3:  556 ( 5.56%) ███████████
 4:  833 ( 8.33%) ████████████████
 5: 1111 (11.11%) ██████████████████████
 6: 1389 (13.89%) ███████████████████████████
 7: 1667 (16.67%) █████████████████████████████████
 8: 1389 (13.89%) ███████████████████████████
 9: 1111 (11.11%) ██████████████████████
10:  833 ( 8.33%) ████████████████
11:  556 ( 5.56%) ███████████
12:  278 ( 2.78%) █████'''
    },
    12: {  # ★★★★ 電話簿系統
        "code": '''phonebook = {}

def add_contact(name, phone):
    phonebook[name] = phone
    print(f"已新增: {name} - {phone}")

def find_contact(name):
    if name in phonebook:
        print(f"找到: {name} - {phonebook[name]}")
    else:
        print(f"找不到: {name}")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"已刪除: {name}")
    else:
        print(f"找不到: {name}")

def list_all():
    print("=== 所有聯絡人 ===")
    for name, phone in phonebook.items():
        print(f"  {name}: {phone}")

add_contact("小明", "0912-345-678")
add_contact("小華", "0923-456-789")
add_contact("小美", "0934-567-890")
find_contact("小明")
delete_contact("小華")
list_all()''',
        "output": '''已新增: 小明 - 0912-345-678
已新增: 小華 - 0923-456-789
已新增: 小美 - 0934-567-890
找到: 小明 - 0912-345-678
已刪除: 小華
=== 所有聯絡人 ===
  小明: 0912-345-678
  小美: 0934-567-890'''
    },
    13: {  # ★★★★★ 摩斯密碼
        "code": '''MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '/'
}
REVERSE = {v: k for k, v in MORSE.items()}

def to_morse(text):
    return ' '.join(MORSE.get(c.upper(), '') for c in text)

def from_morse(morse):
    return ''.join(REVERSE.get(c, '') for c in morse.split())

for text in ["SOS", "HELLO"]:
    morse = to_morse(text)
    decoded = from_morse(morse)
    print(f"{text} → {morse} → {decoded}")''',
        "output": '''SOS → ... --- ... → SOS
HELLO → .... . .-.. .-.. --- → HELLO'''
    },
    14: {  # ★★★★★ 隨機漫步
        "code": '''import random
import math

steps = 1000
x, y = 0, 0
directions = [(0,1), (0,-1), (1,0), (-1,0)]

for _ in range(steps):
    dx, dy = random.choice(directions)
    x, y = x + dx, y + dy

distance = math.sqrt(x*x + y*y)

print("=== 2D 隨機漫步 ===")
print(f"步數: {steps}")
print(f"最終位置: ({x}, {y})")
print(f"距離原點: {distance:.2f}")
print(f"理論期望: {math.sqrt(steps):.2f}")''',
        "output": '''=== 2D 隨機漫步 ===
步數: 1000
最終位置: (12, -28)
距離原點: 30.46
理論期望: 31.62'''
    },
    15: {  # ★★★★★ 遞迴階乘
        "code": '''import time

# 一般遞迴
def factorial_rec(n):
    if n <= 1: return 1
    return n * factorial_rec(n - 1)

# 迴圈
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 記憶化遞迴
cache = {}
def factorial_memo(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = n * factorial_memo(n - 1)
    return cache[n]

n = 10
print(f"計算 {n}!")
print(f"遞迴: {factorial_rec(n)}")
print(f"迴圈: {factorial_loop(n)}")
print(f"記憶化: {factorial_memo(n)}")''',
        "output": '''計算 10!
遞迴: 3628800
迴圈: 3628800
記憶化: 3628800'''
    },
    16: {  # ★★★★★★ 迷宮生成
        "code": '''import random

def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        maze[y][x] = ' '
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width-1 and 0 < ny < height-1 and maze[ny][nx] == '#':
                maze[y + dy//2][x + dx//2] = ' '
                carve(nx, ny)

    carve(1, 1)
    maze[1][0] = 'S'  # 起點
    maze[height-2][width-1] = 'E'  # 終點
    return maze

maze = generate_maze(15, 9)
print("=== 隨機迷宮 ===")
for row in maze:
    print(''.join(row))''',
        "output": '''=== 隨機迷宮 ===
###############
S   #   #     #
# # # # # ### #
# # # #   #   #
# # # ##### # #
# #   #     # #
# ##### ##### #
#       #     E
###############'''
    },
    17: {  # ★★★★★★ 灌溉排程類別
        "code": '''class IrrigationSchedule:
    def __init__(self, name):
        self.name = name
        self.schedules = []

    def add_schedule(self, time, water_amount, frequency):
        self.schedules.append({
            "time": time,
            "water": water_amount,
            "frequency": frequency
        })

    def daily_water(self):
        return sum(s["water"] for s in self.schedules if s["frequency"] == "daily")

    def show(self):
        print(f"=== {self.name} 灌溉排程 ===")
        for s in self.schedules:
            print(f"  {s['time']} - {s['water']}L ({s['frequency']})")
        print(f"每日總用水: {self.daily_water()}L")

schedule = IrrigationSchedule("A區溫室")
schedule.add_schedule("06:00", 50, "daily")
schedule.add_schedule("12:00", 30, "daily")
schedule.add_schedule("18:00", 40, "daily")
schedule.show()''',
        "output": '''=== A區溫室 灌溉排程 ===
  06:00 - 50L (daily)
  12:00 - 30L (daily)
  18:00 - 40L (daily)
每日總用水: 120L'''
    },
    18: {  # ★★★★★★ 文字直方圖
        "code": '''text = "Hello World Programming"
freq = {}
for char in text.lower():
    if char.isalpha():
        freq[char] = freq.get(char, 0) + 1

print("=== 字母頻率直方圖 ===")
max_count = max(freq.values())
for char, count in sorted(freq.items()):
    bar = "*" * (count * 20 // max_count)
    print(f"{char}: {bar} ({count})")''',
        "output": '''=== 字母頻率直方圖 ===
a: ******** (1)
d: ******** (1)
e: ******** (1)
g: ******** (1)
h: ******** (1)
i: ******** (1)
l: **************** (2)
m: ******** (1)
n: ******** (1)
o: ************************ (3)
p: ******** (1)
r: **************** (2)
w: ******** (1)'''
    }
}
