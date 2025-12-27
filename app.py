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

# 各組的題目（每組 6 題：2簡單 + 2中等 + 2困難，互不重複）
GROUP_TASKS = {
    1: {  # 第 1 組：紅隊
        1: "★【變數練習】宣告姓名、年齡、身高三個變數，並印出自我介紹",
        2: "★【空心方形】用 * 符號印出邊長為 8 的空心方形",
        3: "★★【成績統計】建立 10 位學生的成績列表，計算平均、最高、最低、及格人數",
        4: "★★【擲硬幣】模擬擲硬幣 10000 次，統計正反面次數和機率",
        5: "★★★【費氏數列】印出費氏數列前 20 項，並計算第 20 項的值",
        6: "★★★【凱薩密碼】將 'HELLO WORLD' 用位移 3 加密，再解密回來"
    },
    2: {  # 第 2 組：藍隊
        1: "★【計算機】計算 123 + 456、789 - 123、12 * 34、100 / 7 的結果",
        2: "★【數字金字塔】印出數字金字塔（1, 12, 123, 1234...共 9 行）",
        3: "★★【詞頻統計】統計 'to be or not to be that is the question' 每個單字出現次數",
        4: "★★【抽獎模擬】模擬抽獎 1000 次，統計 1/100 中獎率的實際結果",
        5: "★★★【質數篩選】找出 1-100 之間所有的質數",
        6: "★★★【摩斯密碼】將 'SOS' 轉成摩斯密碼，再轉回英文驗證"
    },
    3: {  # 第 3 組：綠隊
        1: "★【字串操作】將 'Hello World' 轉成大寫、小寫、反轉，並計算長度",
        2: "★【重複過濾】從 [1,2,2,3,3,3,4,4,4,4] 中移除重複元素",
        3: "★★【聖誕樹】用 * 符號印出高度為 10 的聖誕樹（三角形加樹幹）",
        4: "★★【最大公因數】實作輾轉相除法，計算 48 和 18 的最大公因數",
        5: "★★★【蒙地卡羅】用隨機投點法估算圓周率（投 100000 個點）",
        6: "★★★【密碼產生器】產生 5 組 12 位隨機密碼，包含大小寫字母、數字和符號"
    },
    4: {  # 第 4 組：黃隊
        1: "★【列表操作】建立 1-10 的列表，印出總和、平均、最大、最小值",
        2: "★【分組統計】將 1-20 分成奇數和偶數兩組，分別計算總和",
        3: "★★【菱形】用 * 符號印出寬度為 9 的菱形",
        4: "★★【氣溫分析】建立一週氣溫資料，找出最熱最冷的日子並計算平均溫度",
        5: "★★★【二分搜尋】電腦隨機產生 1-100 的答案，用二分法自動猜測並印出過程",
        6: "★★★【撲克牌】模擬洗牌並抽 5 張，判斷是否為同花、順子、對子等牌型"
    },
    5: {  # 第 5 組：紫隊
        1: "★【字典練習】建立一個學生資料字典（姓名、學號、成績），並印出內容",
        2: "★【數字轉換】將十進位 255 轉成二進位、八進位、十六進位",
        3: "★★【九九乘法表】印出格式整齊的九九乘法表",
        4: "★★【成績等第】將 [85,72,90,66,58,95,43,77] 轉換成等第（A/B/C/D/F）",
        5: "★★★【生日悖論】模擬 1000 次，驗證 23 人中至少兩人同生日的機率",
        6: "★★★【排序比較】產生 10 個隨機數字，分別用氣泡排序和選擇排序印出過程"
    },
    6: {  # 第 6 組：橙隊
        1: "★【迴圈練習】用 for 迴圈印出 1-100 中所有 3 的倍數",
        2: "★【回文檢查】檢查 'racecar'、'hello'、'level' 是否為回文",
        3: "★★【Pascal 三角形】印出巴斯卡三角形前 10 行",
        4: "★★【骰子統計】模擬擲 2 顆骰子 10000 次，統計每種點數和的機率",
        5: "★★★【河內塔】印出 4 個圓盤的河內塔移動步驟",
        6: "★★★【隨機漫步】模擬 2D 隨機漫步 1000 步，計算最終距離原點的距離"
    }
}

# 各組的執行結果
# 結構: groups_data[group_id][task_id] = {code, output, last_run}
groups_data = {i: {} for i in range(1, 7)}

# ============================================================
# 預設答案資料（展示用，可刪除）
# ============================================================
SAMPLE_ANSWERS = {
    1: {  # 第 1 組：紅隊
        1: {  # ★ 變數練習
            "code": '''name = "小明"
age = 18
height = 170.5

print(f"大家好，我是{name}")
print(f"我今年 {age} 歲")
print(f"我的身高是 {height} 公分")
print(f"很高興認識大家！")''',
            "output": '''大家好，我是小明
我今年 18 歲
我的身高是 170.5 公分
很高興認識大家！'''
        },
        2: {  # ★ 空心方形
            "code": '''size = 8

for i in range(size):
    for j in range(size):
        if i == 0 or i == size-1 or j == 0 or j == size-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()''',
            "output": '''********
*      *
*      *
*      *
*      *
*      *
*      *
********'''
        },
        3: {  # ★★ 成績統計
            "code": '''scores = [85, 72, 90, 66, 58, 95, 43, 77, 88, 61]

print(f"學生成績: {scores}")
print(f"平均分數: {sum(scores) / len(scores):.1f}")
print(f"最高分: {max(scores)}")
print(f"最低分: {min(scores)}")

passing = [s for s in scores if s >= 60]
print(f"及格人數: {len(passing)} 人")
print(f"不及格人數: {len(scores) - len(passing)} 人")''',
            "output": '''學生成績: [85, 72, 90, 66, 58, 95, 43, 77, 88, 61]
平均分數: 73.5
最高分: 95
最低分: 43
及格人數: 8 人
不及格人數: 2 人'''
        },
        4: {  # ★★ 擲硬幣
            "code": '''import random

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
print(f"反面: {tails} 次 ({tails/trials*100:.2f}%)")''',
            "output": '''擲硬幣 10000 次的結果:
正面: 5023 次 (50.23%)
反面: 4977 次 (49.77%)'''
        },
        5: {  # ★★★ 費氏數列
            "code": '''fib = [0, 1]
for i in range(2, 20):
    fib.append(fib[i-1] + fib[i-2])

print("費氏數列前 20 項:")
for i, num in enumerate(fib, 1):
    print(f"第 {i:2d} 項: {num}")

print(f"\\n第 20 項的值是: {fib[19]}")''',
            "output": '''費氏數列前 20 項:
第  1 項: 0
第  2 項: 1
第  3 項: 1
第  4 項: 2
第  5 項: 3
第  6 項: 5
第  7 項: 8
第  8 項: 13
第  9 項: 21
第 10 項: 34
第 11 項: 55
第 12 項: 89
第 13 項: 144
第 14 項: 233
第 15 項: 377
第 16 項: 610
第 17 項: 987
第 18 項: 1597
第 19 項: 2584
第 20 項: 4181

第 20 項的值是: 4181'''
        },
        6: {  # ★★★ 凱薩密碼
            "code": '''def caesar_cipher(text, shift):
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
print(f"解密後: {decrypted}")''',
            "output": '''=== 凱薩密碼 ===
原文: HELLO WORLD
位移: 3
加密後: KHOOR ZRUOG
解密後: HELLO WORLD'''
        }
    },
    2: {  # 第 2 組：藍隊
        1: {  # ★ 計算機
            "code": '''print(f"123 + 456 = {123 + 456}")
print(f"789 - 123 = {789 - 123}")
print(f"12 * 34 = {12 * 34}")
print(f"100 / 7 = {100 / 7:.4f}")''',
            "output": '''123 + 456 = 579
789 - 123 = 666
12 * 34 = 408
100 / 7 = 14.2857'''
        },
        2: {  # ★ 數字金字塔
            "code": '''rows = 9

for i in range(1, rows + 1):
    # 印出前導空格
    spaces = " " * (rows - i)
    # 印出數字
    numbers = "".join(str(j) for j in range(1, i + 1))
    print(spaces + numbers)''',
            "output": '''        1
       12
      123
     1234
    12345
   123456
  1234567
 12345678
123456789'''
        },
        3: {  # ★★ 詞頻統計
            "code": '''text = "to be or not to be that is the question"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"原文: {text}")
print(f"\\n詞頻統計:")
for word, count in sorted(word_count.items(), key=lambda x: -x[1]):
    print(f"  {word}: {count} 次")''',
            "output": '''原文: to be or not to be that is the question

詞頻統計:
  to: 2 次
  be: 2 次
  or: 1 次
  not: 1 次
  that: 1 次
  is: 1 次
  the: 1 次
  question: 1 次'''
        },
        4: {  # ★★ 抽獎模擬
            "code": '''import random

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
print(f"期望中獎次數: {expected:.0f}")''',
            "output": '''=== 抽獎模擬 ===
抽獎次數: 1000
設定中獎率: 1.0%
中獎次數: 11
實際中獎率: 1.1%
期望中獎次數: 10'''
        },
        5: {  # ★★★ 質數篩選
            "code": '''def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(1, 101) if is_prime(n)]

print("1-100 之間的質數:")
print(primes)
print(f"\\n共有 {len(primes)} 個質數")''',
            "output": '''1-100 之間的質數:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

共有 25 個質數'''
        },
        6: {  # ★★★ 摩斯密碼
            "code": '''MORSE_CODE = {
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
print(f"驗證: {'成功' if original == decoded else '失敗'}")''',
            "output": '''=== 摩斯密碼 ===
原文: SOS
摩斯密碼: ... --- ...
解碼後: SOS
驗證: 成功'''
        }
    },
    3: {  # 第 3 組：綠隊
        1: {  # ★ 字串操作
            "code": '''text = "Hello World"

print(f"原始字串: {text}")
print(f"轉大寫: {text.upper()}")
print(f"轉小寫: {text.lower()}")
print(f"反轉: {text[::-1]}")
print(f"長度: {len(text)}")''',
            "output": '''原始字串: Hello World
轉大寫: HELLO WORLD
轉小寫: hello world
反轉: dlroW olleH
長度: 11'''
        },
        2: {  # ★ 重複過濾
            "code": '''original = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

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
print(f"方法三 (dict): {unique_dict}")''',
            "output": '''原始列表: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
方法一 (set): [1, 2, 3, 4]
方法二 (保持順序): [1, 2, 3, 4]
方法三 (dict): [1, 2, 3, 4]'''
        },
        3: {  # ★★ 聖誕樹
            "code": '''height = 10

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
    print(spaces + trunk)''',
            "output": '''         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
        ***
        ***'''
        },
        4: {  # ★★ 最大公因數
            "code": '''def gcd(a, b):
    print(f"計算 GCD({a}, {b})")
    while b != 0:
        print(f"  {a} = {b} × {a // b} + {a % b}")
        a, b = b, a % b
    return a

num1, num2 = 48, 18
result = gcd(num1, num2)
print(f"\\n{num1} 和 {num2} 的最大公因數是: {result}")''',
            "output": '''計算 GCD(48, 18)
  48 = 18 × 2 + 12
  18 = 12 × 1 + 6
  12 = 6 × 2 + 0

48 和 18 的最大公因數是: 6'''
        },
        5: {  # ★★★ 蒙地卡羅
            "code": '''import random

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
print(f"誤差: {abs(pi_estimate - 3.141593):.6f}")''',
            "output": '''=== 蒙地卡羅法估算圓周率 ===
投點數量: 100000
落在圓內的點: 78537
估算的圓周率: 3.141480
實際圓周率: 3.141593
誤差: 0.000113'''
        },
        6: {  # ★★★ 密碼產生器
            "code": '''import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("=== 隨機密碼產生器 ===")
print("產生 5 組 12 位密碼:\\n")

for i in range(1, 6):
    pwd = generate_password(12)
    print(f"密碼 {i}: {pwd}")''',
            "output": '''=== 隨機密碼產生器 ===
產生 5 組 12 位密碼:

密碼 1: Kx9#mP2@vL5n
密碼 2: Qw3&hT8*jR1y
密碼 3: Zc7!bN4#fU6s
密碼 4: Md5@gY9^wE2k
密碼 5: Hp1*tA6!xO8v'''
        }
    },
    4: {  # 第 4 組：黃隊
        1: {  # ★ 列表操作
            "code": '''numbers = list(range(1, 11))

print(f"列表: {numbers}")
print(f"總和: {sum(numbers)}")
print(f"平均: {sum(numbers) / len(numbers)}")
print(f"最大值: {max(numbers)}")
print(f"最小值: {min(numbers)}")''',
            "output": '''列表: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
總和: 55
平均: 5.5
最大值: 10
最小值: 1'''
        },
        2: {  # ★ 分組統計
            "code": '''numbers = list(range(1, 21))

odd = [n for n in numbers if n % 2 == 1]
even = [n for n in numbers if n % 2 == 0]

print(f"1-20 的數字: {numbers}")
print()
print(f"奇數: {odd}")
print(f"奇數總和: {sum(odd)}")
print()
print(f"偶數: {even}")
print(f"偶數總和: {sum(even)}")''',
            "output": '''1-20 的數字: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

奇數: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
奇數總和: 100

偶數: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
偶數總和: 110'''
        },
        3: {  # ★★ 菱形
            "code": '''width = 9
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
    print(spaces + stars)''',
            "output": '''    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *'''
        },
        4: {  # ★★ 氣溫分析
            "code": '''days = ["週一", "週二", "週三", "週四", "週五", "週六", "週日"]
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

print(f"\\n最熱的日子: {hottest} ({max_temp}°C)")
print(f"最冷的日子: {coldest} ({min_temp}°C)")
print(f"平均溫度: {avg_temp:.1f}°C")''',
            "output": '''=== 一週氣溫資料 ===
週一: 28°C
週二: 30°C
週三: 32°C
週四: 29°C
週五: 27°C
週六: 31°C
週日: 33°C

最熱的日子: 週日 (33°C)
最冷的日子: 週五 (27°C)
平均溫度: 30.0°C'''
        },
        5: {  # ★★★ 二分搜尋
            "code": '''import random

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
        high = guess - 1''',
            "output": '''答案是: 73
==============================
開始用二分法猜測:
第 1 次猜測: 50 (範圍: 1-100)
  50 太小了
第 2 次猜測: 75 (範圍: 51-100)
  75 太大了
第 3 次猜測: 63 (範圍: 51-74)
  63 太小了
第 4 次猜測: 69 (範圍: 64-74)
  69 太小了
第 5 次猜測: 72 (範圍: 70-74)
  72 太小了
第 6 次猜測: 73 (範圍: 73-74)
猜對了！答案是 73，共猜了 6 次'''
        },
        6: {  # ★★★ 撲克牌
            "code": '''import random

suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck)
hand = deck[:5]

print("=== 撲克牌判斷 ===")
print(f"抽到的牌: {[f'{r}{s}' for r, s in hand]}")
print()

hand_suits = [s for r, s in hand]
hand_ranks = [r for r, s in hand]

is_flush = len(set(hand_suits)) == 1

rank_values = []
for r in hand_ranks:
    if r == 'A': rank_values.append(1)
    elif r == 'J': rank_values.append(11)
    elif r == 'Q': rank_values.append(12)
    elif r == 'K': rank_values.append(13)
    else: rank_values.append(int(r))

rank_values.sort()
is_straight = (rank_values == list(range(rank_values[0], rank_values[0]+5)))

rank_count = {}
for r in hand_ranks:
    rank_count[r] = rank_count.get(r, 0) + 1
counts = sorted(rank_count.values(), reverse=True)

if is_flush and is_straight: hand_type = "同花順"
elif counts[0] == 4: hand_type = "四條"
elif counts[0] == 3 and counts[1] == 2: hand_type = "葫蘆"
elif is_flush: hand_type = "同花"
elif is_straight: hand_type = "順子"
elif counts[0] == 3: hand_type = "三條"
elif counts[0] == 2 and counts[1] == 2: hand_type = "兩對"
elif counts[0] == 2: hand_type = "一對"
else: hand_type = "散牌"

print(f"牌型: {hand_type}")''',
            "output": '''=== 撲克牌判斷 ===
抽到的牌: ['7♠', 'K♥', '7♦', '3♣', '7♣']

牌型: 三條'''
        }
    },
    5: {  # 第 5 組：紫隊
        1: {  # ★ 字典練習
            "code": '''student = {
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
    print(f"  {subject}: {score} 分")''',
            "output": '''=== 學生資料 ===
姓名: 王小明
學號: A12345678
成績:
  國文: 85 分
  英文: 92 分
  數學: 78 分'''
        },
        2: {  # ★ 數字轉換
            "code": '''decimal = 255

print("=== 進位轉換 ===")
print(f"十進位: {decimal}")
print(f"二進位: {bin(decimal)} = {bin(decimal)[2:]}")
print(f"八進位: {oct(decimal)} = {oct(decimal)[2:]}")
print(f"十六進位: {hex(decimal)} = {hex(decimal)[2:].upper()}")

print("\\n手動轉換二進位過程:")
n = decimal
binary = ""
while n > 0:
    binary = str(n % 2) + binary
    print(f"  {n} ÷ 2 = {n//2} ... {n%2}")
    n //= 2
print(f"結果: {binary}")''',
            "output": '''=== 進位轉換 ===
十進位: 255
二進位: 0b11111111 = 11111111
八進位: 0o377 = 377
十六進位: 0xff = FF

手動轉換二進位過程:
  255 ÷ 2 = 127 ... 1
  127 ÷ 2 = 63 ... 1
  63 ÷ 2 = 31 ... 1
  31 ÷ 2 = 15 ... 1
  15 ÷ 2 = 7 ... 1
  7 ÷ 2 = 3 ... 1
  3 ÷ 2 = 1 ... 1
  1 ÷ 2 = 0 ... 1
結果: 11111111'''
        },
        3: {  # ★★ 九九乘法表
            "code": '''print("=== 九九乘法表 ===")
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
    print()''',
            "output": '''=== 九九乘法表 ===

       1   2   3   4   5   6   7   8   9
    ------------------------------------
 1 |   1   2   3   4   5   6   7   8   9
 2 |   2   4   6   8  10  12  14  16  18
 3 |   3   6   9  12  15  18  21  24  27
 4 |   4   8  12  16  20  24  28  32  36
 5 |   5  10  15  20  25  30  35  40  45
 6 |   6  12  18  24  30  36  42  48  54
 7 |   7  14  21  28  35  42  49  56  63
 8 |   8  16  24  32  40  48  56  64  72
 9 |   9  18  27  36  45  54  63  72  81'''
        },
        4: {  # ★★ 成績等第
            "code": '''scores = [85, 72, 90, 66, 58, 95, 43, 77]

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

grades = [get_grade(s) for s in scores]
print("\\n等第分布:")
for g in ['A', 'B', 'C', 'D', 'F']:
    count = grades.count(g)
    print(f"  {g}: {count} 人")''',
            "output": '''成績等第轉換:
--------------------
85 分 → B
72 分 → C
90 分 → A
66 分 → D
58 分 → F
95 分 → A
43 分 → F
77 分 → C

等第分布:
  A: 2 人
  B: 1 人
  C: 2 人
  D: 1 人
  F: 2 人'''
        },
        5: {  # ★★★ 生日悖論
            "code": '''import random

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
print(f"理論機率: 約 50.7%")''',
            "output": '''=== 生日悖論模擬 ===
模擬次數: 1000
人數: 23 人
有重複生日的次數: 512
實驗機率: 51.2%
理論機率: 約 50.7%'''
        },
        6: {  # ★★★ 排序比較
            "code": '''import random

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
    print(f"第 {i+1} 輪: {arr}")''',
            "output": '''原始數列: [64, 34, 25, 12, 22, 11, 90, 45, 33, 77]

=== 氣泡排序 ===
第 1 輪: [34, 25, 12, 22, 11, 64, 45, 33, 77, 90]
第 2 輪: [25, 12, 22, 11, 34, 45, 33, 64, 77, 90]
第 3 輪: [12, 22, 11, 25, 34, 33, 45, 64, 77, 90]
第 4 輪: [12, 11, 22, 25, 33, 34, 45, 64, 77, 90]
第 5 輪: [11, 12, 22, 25, 33, 34, 45, 64, 77, 90]
第 6 輪: [11, 12, 22, 25, 33, 34, 45, 64, 77, 90]
第 7 輪: [11, 12, 22, 25, 33, 34, 45, 64, 77, 90]
第 8 輪: [11, 12, 22, 25, 33, 34, 45, 64, 77, 90]
第 9 輪: [11, 12, 22, 25, 33, 34, 45, 64, 77, 90]
第 10 輪: [11, 12, 22, 25, 33, 34, 45, 64, 77, 90]

=== 選擇排序 ===
第 1 輪: [11, 34, 25, 12, 22, 64, 90, 45, 33, 77]
第 2 輪: [11, 12, 25, 34, 22, 64, 90, 45, 33, 77]
第 3 輪: [11, 12, 22, 34, 25, 64, 90, 45, 33, 77]
第 4 輪: [11, 12, 22, 25, 34, 64, 90, 45, 33, 77]
第 5 輪: [11, 12, 22, 25, 33, 64, 90, 45, 34, 77]
第 6 輪: [11, 12, 22, 25, 33, 34, 90, 45, 64, 77]
第 7 輪: [11, 12, 22, 25, 33, 34, 45, 90, 64, 77]
第 8 輪: [11, 12, 22, 25, 33, 34, 45, 64, 90, 77]
第 9 輪: [11, 12, 22, 25, 33, 34, 45, 64, 77, 90]
第 10 輪: [11, 12, 22, 25, 33, 34, 45, 64, 77, 90]'''
        }
    },
    6: {  # 第 6 組：橙隊
        1: {  # ★ 迴圈練習
            "code": '''print("1-100 中所有 3 的倍數:")
multiples = []
for i in range(1, 101):
    if i % 3 == 0:
        multiples.append(i)

print(multiples)
print(f"共有 {len(multiples)} 個")''',
            "output": '''1-100 中所有 3 的倍數:
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
共有 33 個'''
        },
        2: {  # ★ 回文檢查
            "code": '''def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

words = ['racecar', 'hello', 'level']

print("=== 回文檢查 ===")
for word in words:
    reversed_word = word[::-1]
    result = "是回文" if is_palindrome(word) else "不是回文"
    print(f"'{word}' 反轉後是 '{reversed_word}' → {result}")''',
            "output": '''=== 回文檢查 ===
'racecar' 反轉後是 'racecar' → 是回文
'hello' 反轉後是 'olleh' → 不是回文
'level' 反轉後是 'level' → 是回文'''
        },
        3: {  # ★★ Pascal 三角形
            "code": '''rows = 10
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
    print(row_str.center(max_width))''',
            "output": '''巴斯卡三角形前 10 行:

                       1
                      1 1
                     1 2 1
                    1 3 3 1
                   1 4 6 4 1
                 1 5 10 10 5 1
               1 6 15 20 15 6 1
              1 7 21 35 35 21 7 1
            1 8 28 56 70 56 28 8 1
          1 9 36 84 126 126 84 36 9 1           '''
        },
        4: {  # ★★ 骰子統計
            "code": '''import random

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
    print(f"點數和 {total:2d}: {count:4d} 次 ({prob:5.2f}%) {bar}")''',
            "output": '''擲 2 顆骰子 10000 次的點數和分布:
-----------------------------------
點數和  2:  271 次 ( 2.71%) █████
點數和  3:  548 次 ( 5.48%) ██████████
點數和  4:  842 次 ( 8.42%) ████████████████
點數和  5: 1089 次 (10.89%) █████████████████████
點數和  6: 1402 次 (14.02%) ████████████████████████████
點數和  7: 1668 次 (16.68%) █████████████████████████████████
點數和  8: 1385 次 (13.85%) ███████████████████████████
點數和  9: 1115 次 (11.15%) ██████████████████████
點數和 10:  834 次 ( 8.34%) ████████████████
點數和 11:  556 次 ( 5.56%) ███████████
點數和 12:  290 次 ( 2.90%) █████'''
        },
        5: {  # ★★★ 河內塔
            "code": '''def hanoi(n, source, target, auxiliary, step=[0]):
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
print(f"\\n總共需要 {2**4 - 1} 步")''',
            "output": '''河內塔 - 4 個圓盤的移動步驟:
(A: 起始柱, B: 輔助柱, C: 目標柱)
========================================
步驟  1: 將圓盤 1 從 A 移到 B
步驟  2: 將圓盤 2 從 A 移到 C
步驟  3: 將圓盤 1 從 B 移到 C
步驟  4: 將圓盤 3 從 A 移到 B
步驟  5: 將圓盤 1 從 C 移到 A
步驟  6: 將圓盤 2 從 C 移到 B
步驟  7: 將圓盤 1 從 A 移到 B
步驟  8: 將圓盤 4 從 A 移到 C
步驟  9: 將圓盤 1 從 B 移到 C
步驟 10: 將圓盤 2 從 B 移到 A
步驟 11: 將圓盤 1 從 C 移到 A
步驟 12: 將圓盤 3 從 B 移到 C
步驟 13: 將圓盤 1 從 A 移到 B
步驟 14: 將圓盤 2 從 A 移到 C
步驟 15: 將圓盤 1 從 B 移到 C

總共需要 15 步'''
        },
        6: {  # ★★★ 隨機漫步
            "code": '''import random
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
print(f"理論期望距離: {math.sqrt(steps):.2f}")''',
            "output": '''=== 2D 隨機漫步 ===
步數: 1000
最終位置: (12, -28)
距離原點: 30.46
理論期望距離: 31.62'''
        }
    }
}


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
            "total": 6  # 每組固定 6 題
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
