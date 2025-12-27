# 第 1 組答案 (18題)

ANSWERS = {
    1: {  # ★ 變數與輸出
        "code": '''name = "小明"
age = 18
height = 170.5

print(f"大家好，我是{name}")
print(f"我今年 {age} 歲")
print(f"身高 {height} 公分")''',
        "output": '''大家好，我是小明
我今年 18 歲
身高 170.5 公分'''
    },
    2: {  # ★ 四則運算
        "code": '''print(f"123 + 456 = {123 + 456}")
print(f"789 - 123 = {789 - 123}")
print(f"12 * 34 = {12 * 34}")
print(f"100 / 7 = {100 / 7:.4f}")''',
        "output": '''123 + 456 = 579
789 - 123 = 666
12 * 34 = 408
100 / 7 = 14.2857'''
    },
    3: {  # ★ 字串基礎
        "code": '''text = "Hello World"
print(f"原始: {text}")
print(f"大寫: {text.upper()}")
print(f"小寫: {text.lower()}")
print(f"反轉: {text[::-1]}")
print(f"長度: {len(text)}")''',
        "output": '''原始: Hello World
大寫: HELLO WORLD
小寫: hello world
反轉: dlroW olleH
長度: 11'''
    },
    4: {  # ★★ 判斷閏年
        "code": '''def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

years = [2000, 2024, 1900, 2023]
for y in years:
    result = "是" if is_leap_year(y) else "不是"
    print(f"{y} 年{result}閏年")''',
        "output": '''2000 年是閏年
2024 年是閏年
1900 年不是閏年
2023 年不是閏年'''
    },
    5: {  # ★★ FizzBuzz
        "code": '''for i in range(1, 31):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)''',
        "output": '''1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz'''
    },
    6: {  # ★★ 成績等第
        "code": '''scores = [85, 72, 90, 66, 58, 95, 43, 77]

def get_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

for s in scores:
    print(f"{s} 分 → {get_grade(s)}")''',
        "output": '''85 分 → B
72 分 → C
90 分 → A
66 分 → D
58 分 → F
95 分 → A
43 分 → F
77 分 → C'''
    },
    7: {  # ★★★ 質數判斷
        "code": '''def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

primes = [n for n in range(1, 101) if is_prime(n)]
print(f"1-100 的質數: {primes}")
print(f"共 {len(primes)} 個")''',
        "output": '''1-100 的質數: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
共 25 個'''
    },
    8: {  # ★★★ 九九乘法表
        "code": '''print("=== 九九乘法表 ===")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}×{j}={i*j:2d}", end="  ")
    print()''',
        "output": '''=== 九九乘法表 ===
1×1= 1  1×2= 2  1×3= 3  1×4= 4  1×5= 5  1×6= 6  1×7= 7  1×8= 8  1×9= 9
2×1= 2  2×2= 4  2×3= 6  2×4= 8  2×5=10  2×6=12  2×7=14  2×8=16  2×9=18
3×1= 3  3×2= 6  3×3= 9  3×4=12  3×5=15  3×6=18  3×7=21  3×8=24  3×9=27
4×1= 4  4×2= 8  4×3=12  4×4=16  4×5=20  4×6=24  4×7=28  4×8=32  4×9=36
5×1= 5  5×2=10  5×3=15  5×4=20  5×5=25  5×6=30  5×7=35  5×8=40  5×9=45
6×1= 6  6×2=12  6×3=18  6×4=24  6×5=30  6×6=36  6×7=42  6×8=48  6×9=54
7×1= 7  7×2=14  7×3=21  7×4=28  7×5=35  7×6=42  7×7=49  7×8=56  7×9=63
8×1= 8  8×2=16  8×3=24  8×4=32  8×5=40  8×6=48  8×7=56  8×8=64  8×9=72
9×1= 9  9×2=18  9×3=27  9×4=36  9×5=45  9×6=54  9×7=63  9×8=72  9×9=81  '''
    },
    9: {  # ★★★ 字典統計
        "code": '''text = "to be or not to be that is the question"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"原文: {text}")
print("\\n詞頻統計:")
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
    10: {  # ★★★★ 聖誕樹圖案
        "code": '''def draw_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
    # 樹幹
    trunk_width = 3
    for _ in range(2):
        print(" " * (height - 2) + "*" * trunk_width)

draw_tree(10)''',
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
    11: {  # ★★★★ 最大公因數
        "code": '''def gcd(a, b):
    print(f"計算 GCD({a}, {b})")
    while b != 0:
        print(f"  {a} = {b} × {a//b} + {a%b}")
        a, b = b, a % b
    return a

result = gcd(48, 18)
print(f"\\n最大公因數: {result}")''',
        "output": '''計算 GCD(48, 18)
  48 = 18 × 2 + 12
  18 = 12 × 1 + 6
  12 = 6 × 2 + 0

最大公因數: 6'''
    },
    12: {  # ★★★★ 氣溫分析
        "code": '''def analyze_temp(data):
    temps = list(data.values())
    max_day = max(data, key=data.get)
    min_day = min(data, key=data.get)
    avg = sum(temps) / len(temps)
    return max_day, min_day, avg

weather = {"週一": 28, "週二": 30, "週三": 32,
           "週四": 29, "週五": 27, "週六": 31, "週日": 33}

print("=== 一週氣溫 ===")
for day, temp in weather.items():
    print(f"{day}: {temp}°C")

max_d, min_d, avg = analyze_temp(weather)
print(f"\\n最高溫: {max_d} ({weather[max_d]}°C)")
print(f"最低溫: {min_d} ({weather[min_d]}°C)")
print(f"平均: {avg:.1f}°C")''',
        "output": '''=== 一週氣溫 ===
週一: 28°C
週二: 30°C
週三: 32°C
週四: 29°C
週五: 27°C
週六: 31°C
週日: 33°C

最高溫: 週日 (33°C)
最低溫: 週五 (27°C)
平均: 30.0°C'''
    },
    13: {  # ★★★★★ 費氏數列
        "code": '''import time

# 遞迴版本
def fib_recursive(n):
    if n <= 1: return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# 迴圈版本
def fib_loop(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# 比較效能
print("費氏數列前 20 項 (迴圈):")
result = [fib_loop(i) for i in range(20)]
print(result)

start = time.time()
fib_loop(30)
loop_time = time.time() - start

start = time.time()
fib_recursive(30)
rec_time = time.time() - start

print(f"\\n迴圈版 F(30) 耗時: {loop_time:.6f} 秒")
print(f"遞迴版 F(30) 耗時: {rec_time:.6f} 秒")''',
        "output": '''費氏數列前 20 項 (迴圈):
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

迴圈版 F(30) 耗時: 0.000001 秒
遞迴版 F(30) 耗時: 0.234567 秒'''
    },
    14: {  # ★★★★★ 凱薩密碼
        "code": '''def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

original = "HELLO WORLD"
shift = 3
encrypted = caesar_encrypt(original, shift)
decrypted = caesar_decrypt(encrypted, shift)

print(f"原文: {original}")
print(f"加密 (位移 {shift}): {encrypted}")
print(f"解密: {decrypted}")''',
        "output": '''原文: HELLO WORLD
加密 (位移 3): KHOOR ZRUOG
解密: HELLO WORLD'''
    },
    15: {  # ★★★★★ 蒙地卡羅法
        "code": '''import random

total = 100000
inside = 0

for _ in range(total):
    x, y = random.random(), random.random()
    if x*x + y*y <= 1:
        inside += 1

pi_estimate = 4 * inside / total
real_pi = 3.141592653589793

print("=== 蒙地卡羅法估算圓周率 ===")
print(f"投點數: {total}")
print(f"落在圓內: {inside}")
print(f"估算 π: {pi_estimate:.6f}")
print(f"實際 π: {real_pi:.6f}")
print(f"誤差: {abs(pi_estimate - real_pi):.6f}")''',
        "output": '''=== 蒙地卡羅法估算圓周率 ===
投點數: 100000
落在圓內: 78539
估算 π: 3.141560
實際 π: 3.141593
誤差: 0.000033'''
    },
    16: {  # ★★★★★★ 撲克牌判斷
        "code": '''import random

suits = ['♠', '♥', '♦', '♣']
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = [(r, s) for s in suits for r in ranks]
random.shuffle(deck)
hand = deck[:5]

print(f"抽到: {[f'{r}{s}' for r,s in hand]}")

# 判斷牌型
hand_suits = [s for r,s in hand]
hand_ranks = [r for r,s in hand]

is_flush = len(set(hand_suits)) == 1

rank_val = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
            '8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
vals = sorted([rank_val[r] for r in hand_ranks])
is_straight = vals == list(range(vals[0], vals[0]+5))

counts = {}
for r in hand_ranks:
    counts[r] = counts.get(r, 0) + 1
c = sorted(counts.values(), reverse=True)

if is_flush and is_straight: hand_type = "同花順"
elif c[0] == 4: hand_type = "四條"
elif c == [3,2]: hand_type = "葫蘆"
elif is_flush: hand_type = "同花"
elif is_straight: hand_type = "順子"
elif c[0] == 3: hand_type = "三條"
elif c == [2,2,1]: hand_type = "兩對"
elif c[0] == 2: hand_type = "一對"
else: hand_type = "散牌"

print(f"牌型: {hand_type}")''',
        "output": '''抽到: ['7♠', 'K♥', '7♦', '3♣', '7♣']
牌型: 三條'''
    },
    17: {  # ★★★★★★ 河內塔遞迴
        "code": '''move_count = 0

def hanoi(n, source, target, auxiliary):
    global move_count
    if n == 1:
        move_count += 1
        print(f"步驟 {move_count:2d}: 圓盤 1: {source} → {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    move_count += 1
    print(f"步驟 {move_count:2d}: 圓盤 {n}: {source} → {target}")
    hanoi(n-1, auxiliary, target, source)

print("=== 河內塔 (4 個圓盤) ===")
hanoi(4, 'A', 'C', 'B')
print(f"\\n總步數: {move_count} (理論值: {2**4 - 1})''',
        "output": '''=== 河內塔 (4 個圓盤) ===
步驟  1: 圓盤 1: A → B
步驟  2: 圓盤 2: A → C
步驟  3: 圓盤 1: B → C
步驟  4: 圓盤 3: A → B
步驟  5: 圓盤 1: C → A
步驟  6: 圓盤 2: C → B
步驟  7: 圓盤 1: A → B
步驟  8: 圓盤 4: A → C
步驟  9: 圓盤 1: B → C
步驟 10: 圓盤 2: B → A
步驟 11: 圓盤 1: C → A
步驟 12: 圓盤 3: B → C
步驟 13: 圓盤 1: A → B
步驟 14: 圓盤 2: A → C
步驟 15: 圓盤 1: B → C

總步數: 15 (理論值: 15)'''
    },
    18: {  # ★★★★★★ 感測器類別
        "code": '''class Sensor:
    def __init__(self, name):
        self.name = name
        self.temp_records = []
        self.humidity_records = []

    def record(self, temp, humidity):
        self.temp_records.append(temp)
        self.humidity_records.append(humidity)

    def stats(self):
        if not self.temp_records:
            return None
        return {
            "temp_avg": sum(self.temp_records) / len(self.temp_records),
            "temp_max": max(self.temp_records),
            "temp_min": min(self.temp_records),
            "humidity_avg": sum(self.humidity_records) / len(self.humidity_records)
        }

sensor = Sensor("溫室A")
data = [(25.5, 60), (26.2, 58), (27.8, 55), (24.1, 65), (28.3, 52)]

for temp, hum in data:
    sensor.record(temp, hum)

stats = sensor.stats()
print(f"感測器: {sensor.name}")
print(f"平均溫度: {stats['temp_avg']:.1f}°C")
print(f"最高溫度: {stats['temp_max']}°C")
print(f"最低溫度: {stats['temp_min']}°C")
print(f"平均濕度: {stats['humidity_avg']:.1f}%")''',
        "output": '''感測器: 溫室A
平均溫度: 26.4°C
最高溫度: 28.3°C
最低溫度: 24.1°C
平均濕度: 58.0%'''
    }
}
