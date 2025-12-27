# 第 2 組答案 (18題)

ANSWERS = {
    1: {  # ★ 型別轉換
        "code": '''str_int = "123"
str_float = "3.14"

num_int = int(str_int)
num_float = float(str_float)

print(f"'{str_int}' → {num_int} (型別: {type(num_int).__name__})")
print(f"'{str_float}' → {num_float} (型別: {type(num_float).__name__})")''',
        "output": ''''123' → 123 (型別: int)
'3.14' → 3.14 (型別: float)'''
    },
    2: {  # ★ 列表基礎
        "code": '''numbers = list(range(1, 11))
print(f"列表: {numbers}")
print(f"總和: {sum(numbers)}")
print(f"平均: {sum(numbers)/len(numbers)}")
print(f"最大: {max(numbers)}")
print(f"最小: {min(numbers)}")''',
        "output": '''列表: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
總和: 55
平均: 5.5
最大: 10
最小: 1'''
    },
    3: {  # ★ 布林運算
        "code": '''print(f"5 > 3 = {5 > 3}")
print(f"10 == 10 = {10 == 10}")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")
print(f"(5 > 3) and (10 == 10) = {(5 > 3) and (10 == 10)}")''',
        "output": '''5 > 3 = True
10 == 10 = True
True and False = False
True or False = True
not True = False
(5 > 3) and (10 == 10) = True'''
    },
    4: {  # ★★ 猜數字提示
        "code": '''def guess_hint(guess, answer):
    if guess > answer:
        return "太大"
    elif guess < answer:
        return "太小"
    else:
        return "正確"

answer = 50
tests = [25, 75, 50, 30, 60]
print(f"答案: {answer}")
for g in tests:
    print(f"猜 {g}: {guess_hint(g, answer)}")''',
        "output": '''答案: 50
猜 25: 太小
猜 75: 太大
猜 50: 正確
猜 30: 太小
猜 60: 太大'''
    },
    5: {  # ★★ 數字金字塔
        "code": '''rows = 9
for i in range(1, rows + 1):
    nums = "".join(str(j) for j in range(1, i + 1))
    spaces = " " * (rows - i)
    print(spaces + nums)''',
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
    6: {  # ★★ 奇偶分組
        "code": '''numbers = list(range(1, 21))
odd = [n for n in numbers if n % 2 == 1]
even = [n for n in numbers if n % 2 == 0]

print(f"1-20: {numbers}")
print(f"奇數: {odd}")
print(f"奇數和: {sum(odd)}")
print(f"偶數: {even}")
print(f"偶數和: {sum(even)}")''',
        "output": '''1-20: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
奇數: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
奇數和: 100
偶數: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
偶數和: 110'''
    },
    7: {  # ★★★ 重複過濾
        "code": '''original = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"原始: {original}")

# 方法一: set
unique1 = list(set(original))
print(f"方法1 (set): {sorted(unique1)}")

# 方法二: 迴圈
unique2 = []
for item in original:
    if item not in unique2:
        unique2.append(item)
print(f"方法2 (迴圈): {unique2}")

# 方法三: dict
unique3 = list(dict.fromkeys(original))
print(f"方法3 (dict): {unique3}")''',
        "output": '''原始: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
方法1 (set): [1, 2, 3, 4]
方法2 (迴圈): [1, 2, 3, 4]
方法3 (dict): [1, 2, 3, 4]'''
    },
    8: {  # ★★★ 巴斯卡三角形
        "code": '''rows = 10
triangle = []
for i in range(rows):
    row = [1]
    if i > 0:
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
    triangle.append(row)

print("巴斯卡三角形:")
for row in triangle:
    print(" ".join(f"{n:3d}" for n in row).center(40))''',
        "output": '''巴斯卡三角形:
                  1
                 1   1
                1   2   1
               1   3   3   1
              1   4   6   4   1
            1   5  10  10   5   1
           1   6  15  20  15   6   1
          1   7  21  35  35  21   7   1
        1   8  28  56  70  56  28   8   1
       1   9  36  84 126 126  84  36   9   1'''
    },
    9: {  # ★★★ 進位轉換
        "code": '''decimal = 255
print(f"十進位: {decimal}")
print(f"二進位: {bin(decimal)} = {bin(decimal)[2:]}")
print(f"八進位: {oct(decimal)} = {oct(decimal)[2:]}")
print(f"十六進位: {hex(decimal)} = {hex(decimal)[2:].upper()}")

print("\\n手動轉二進位:")
n = decimal
binary = ""
while n > 0:
    binary = str(n % 2) + binary
    print(f"  {n} ÷ 2 = {n//2} 餘 {n%2}")
    n //= 2
print(f"結果: {binary}")''',
        "output": '''十進位: 255
二進位: 0b11111111 = 11111111
八進位: 0o377 = 377
十六進位: 0xff = FF

手動轉二進位:
  255 ÷ 2 = 127 餘 1
  127 ÷ 2 = 63 餘 1
  63 ÷ 2 = 31 餘 1
  31 ÷ 2 = 15 餘 1
  15 ÷ 2 = 7 餘 1
  7 ÷ 2 = 3 餘 1
  3 ÷ 2 = 1 餘 1
  1 ÷ 2 = 0 餘 1
結果: 11111111'''
    },
    10: {  # ★★★★ 菱形圖案
        "code": '''def draw_diamond(width):
    mid = width // 2 + 1
    # 上半部
    for i in range(1, mid + 1):
        spaces = " " * (mid - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
    # 下半部
    for i in range(mid - 1, 0, -1):
        spaces = " " * (mid - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

draw_diamond(9)''',
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
    11: {  # ★★★★ 擲硬幣模擬
        "code": '''import random

trials = 10000
heads = sum(1 for _ in range(trials) if random.choice([0,1]) == 0)
tails = trials - heads

print(f"擲硬幣 {trials} 次:")
print(f"正面: {heads} 次 ({heads/trials*100:.2f}%)")
print(f"反面: {tails} 次 ({tails/trials*100:.2f}%)")''',
        "output": '''擲硬幣 10000 次:
正面: 5023 次 (50.23%)
反面: 4977 次 (49.77%)'''
    },
    12: {  # ★★★★ 密碼驗證器
        "code": '''def validate_password(pwd):
    errors = []
    if len(pwd) < 8:
        errors.append("長度需 8 位以上")
    if not any(c.isupper() for c in pwd):
        errors.append("需含大寫字母")
    if not any(c.islower() for c in pwd):
        errors.append("需含小寫字母")
    if not any(c.isdigit() for c in pwd):
        errors.append("需含數字")
    if not any(c in "!@#$%^&*" for c in pwd):
        errors.append("需含特殊符號")
    return errors

tests = ["abc", "Abc12345", "Abc123!@"]
for pwd in tests:
    errors = validate_password(pwd)
    status = "通過" if not errors else f"失敗: {errors}"
    print(f"'{pwd}' → {status}")''',
        "output": ''''abc' → 失敗: ['長度需 8 位以上', '需含大寫字母', '需含數字', '需含特殊符號']
'Abc12345' → 失敗: ['需含特殊符號']
'Abc123!@' → 通過'''
    },
    13: {  # ★★★★★ 二分搜尋法
        "code": '''import random

answer = random.randint(1, 100)
print(f"答案: {answer}")
print("=" * 30)

low, high = 1, 100
count = 0
while low <= high:
    count += 1
    guess = (low + high) // 2
    print(f"第 {count} 次: 猜 {guess} (範圍 {low}-{high})")
    if guess == answer:
        print(f"猜對了! 共 {count} 次")
        break
    elif guess < answer:
        print(f"  太小")
        low = guess + 1
    else:
        print(f"  太大")
        high = guess - 1''',
        "output": '''答案: 73
==============================
第 1 次: 猜 50 (範圍 1-100)
  太小
第 2 次: 猜 75 (範圍 51-100)
  太大
第 3 次: 猜 63 (範圍 51-74)
  太小
第 4 次: 猜 69 (範圍 64-74)
  太小
第 5 次: 猜 72 (範圍 70-74)
  太小
第 6 次: 猜 73 (範圍 73-74)
猜對了! 共 6 次'''
    },
    14: {  # ★★★★★ 質數篩法
        "code": '''def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            print(f"篩掉 {i} 的倍數: ", end="")
            removed = []
            for j in range(i*i, n + 1, i):
                if is_prime[j]:
                    is_prime[j] = False
                    removed.append(j)
            print(removed[:10], "..." if len(removed) > 10 else "")

    return [i for i in range(n + 1) if is_prime[i]]

primes = sieve_of_eratosthenes(100)
print(f"\\n1-100 質數: {primes}")
print(f"共 {len(primes)} 個")''',
        "output": '''篩掉 2 的倍數: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22] ...
篩掉 3 的倍數: [9, 15, 21, 27, 33, 39, 45, 51, 57, 63] ...
篩掉 5 的倍數: [25, 35, 55, 65, 85, 95]
篩掉 7 的倍數: [49, 77, 91]

1-100 質數: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
共 25 個'''
    },
    15: {  # ★★★★★ 生日悖論
        "code": '''import random

def birthday_simulation(people, trials):
    matches = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(people)]
        if len(birthdays) != len(set(birthdays)):
            matches += 1
    return matches / trials * 100

print("=== 生日悖論模擬 ===")
for people in [10, 23, 30, 50]:
    prob = birthday_simulation(people, 1000)
    print(f"{people} 人: {prob:.1f}% 有相同生日")''',
        "output": '''=== 生日悖論模擬 ===
10 人: 11.7% 有相同生日
23 人: 50.8% 有相同生日
30 人: 70.5% 有相同生日
50 人: 97.1% 有相同生日'''
    },
    16: {  # ★★★★★★ 排序動畫
        "code": '''import random

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    print("=== 氣泡排序 ===")
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"第 {i+1} 輪: {arr}")
    return arr

def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    print("\\n=== 選擇排序 ===")
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"第 {i+1} 輪: {arr}")
    return arr

original = [64, 34, 25, 12, 22, 11, 90, 45, 33, 77]
print(f"原始: {original}")
bubble_sort(original)
selection_sort(original)''',
        "output": '''原始: [64, 34, 25, 12, 22, 11, 90, 45, 33, 77]
=== 氣泡排序 ===
第 1 輪: [34, 25, 12, 22, 11, 64, 45, 33, 77, 90]
第 2 輪: [25, 12, 22, 11, 34, 45, 33, 64, 77, 90]
...略...

=== 選擇排序 ===
第 1 輪: [11, 34, 25, 12, 22, 64, 90, 45, 33, 77]
第 2 輪: [11, 12, 25, 34, 22, 64, 90, 45, 33, 77]
...略...'''
    },
    17: {  # ★★★★★★ 密碼產生器
        "code": '''import random
import string

def generate_strong_password(length=16):
    # 確保包含各類字元
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*")

    # 填滿剩餘長度
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    remaining = [random.choice(all_chars) for _ in range(length - 4)]

    # 混合並打亂
    password = list(upper + lower + digit + special) + remaining
    random.shuffle(password)
    return "".join(password)

print("=== 強密碼產生器 ===")
for i in range(1, 6):
    pwd = generate_strong_password(16)
    print(f"密碼 {i}: {pwd}")''',
        "output": '''=== 強密碼產生器 ===
密碼 1: Kx9#mP2@vL5nBqTh
密碼 2: Qw3&hT8*jR1yFcNz
密碼 3: Zc7!bN4#fU6sMpYe
密碼 4: Md5@gY9^wE2kHxJt
密碼 5: Hp1*tA6!xO8vDrLq'''
    },
    18: {  # ★★★★★★ 作物產量類別
        "code": '''from datetime import datetime, timedelta

class Crop:
    def __init__(self, name, plant_date):
        self.name = name
        self.plant_date = datetime.strptime(plant_date, "%Y-%m-%d")
        self.yields = []

    def add_yield(self, amount):
        self.yields.append(amount)

    def days_since_plant(self):
        return (datetime.now() - self.plant_date).days

    def total_yield(self):
        return sum(self.yields)

    def report(self):
        print(f"作物: {self.name}")
        print(f"種植日: {self.plant_date.strftime('%Y-%m-%d')}")
        print(f"生長天數: {self.days_since_plant()} 天")
        print(f"收成次數: {len(self.yields)}")
        print(f"總產量: {self.total_yield()} kg")

tomato = Crop("番茄", "2024-09-01")
tomato.add_yield(15.5)
tomato.add_yield(20.3)
tomato.add_yield(18.7)
tomato.report()''',
        "output": '''作物: 番茄
種植日: 2024-09-01
生長天數: 118 天
收成次數: 3
總產量: 54.5 kg'''
    }
}
