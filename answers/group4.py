# 第 4 組答案 (18題)

ANSWERS = {
    1: {  # ★ 輸入輸出
        "code": '''# 使用預設值示範
name = "小明"
age = 18

print(f"歡迎 {name}！")
print(f"您今年 {age} 歲")
print(f"明年您將 {age + 1} 歲")''',
        "output": '''歡迎 小明！
您今年 18 歲
明年您將 19 歲'''
    },
    2: {  # ★ 數學函式
        "code": '''import math

print(f"sqrt(16) = {math.sqrt(16)}")
print(f"π = {math.pi:.6f}")
print(f"sin(90°) = {math.sin(math.radians(90)):.6f}")
print(f"log(100) = {math.log10(100)}")
print(f"e = {math.e:.6f}")''',
        "output": '''sqrt(16) = 4.0
π = 3.141593
sin(90°) = 1.000000
log(100) = 2.0
e = 2.718282'''
    },
    3: {  # ★ 隨機數
        "code": '''import random

nums = [random.randint(1, 100) for _ in range(5)]
print(f"隨機數: {nums}")
print(f"最大值: {max(nums)}")
print(f"最小值: {min(nums)}")
print(f"平均值: {sum(nums)/len(nums):.1f}")''',
        "output": '''隨機數: [42, 87, 15, 63, 29]
最大值: 87
最小值: 15
平均值: 47.2'''
    },
    4: {  # ★★ 溫度轉換
        "code": '''def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

print("攝氏 → 華氏:")
for c in [0, 100]:
    print(f"  {c}°C = {c_to_f(c):.1f}°F")

print("\\n華氏 → 攝氏:")
for f in [32, 212]:
    print(f"  {f}°F = {f_to_c(f):.1f}°C")''',
        "output": '''攝氏 → 華氏:
  0°C = 32.0°F
  100°C = 212.0°F

華氏 → 攝氏:
  32°F = 0.0°C
  212°F = 100.0°C'''
    },
    5: {  # ★★ 星星三角形
        "code": '''height = 5
for i in range(1, height + 1):
    print("*" * i)''',
        "output": '''*
**
***
****
*****'''
    },
    6: {  # ★★ 列表操作
        "code": '''nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"原始: {nums}")

sorted_nums = sorted(nums)
print(f"排序: {sorted_nums}")

reversed_nums = nums[::-1]
print(f"反轉: {reversed_nums}")

nums.insert(0, 0)
print(f"插入0: {nums}")

nums.remove(1)
print(f"刪除1: {nums}")''',
        "output": '''原始: [3, 1, 4, 1, 5, 9, 2, 6]
排序: [1, 1, 2, 3, 4, 5, 6, 9]
反轉: [6, 2, 9, 5, 1, 4, 1, 3]
插入0: [0, 3, 1, 4, 1, 5, 9, 2, 6]
刪除1: [0, 3, 4, 1, 5, 9, 2, 6]'''
    },
    7: {  # ★★★ 因數分解
        "code": '''def find_factors(n):
    factors = [i for i in range(1, n+1) if n % i == 0]
    return factors

for num in [36, 100, 97]:
    factors = find_factors(num)
    print(f"{num} 的因數: {factors}")
    if len(factors) == 2:
        print(f"  → {num} 是質數")''',
        "output": '''36 的因數: [1, 2, 3, 4, 6, 9, 12, 18, 36]
100 的因數: [1, 2, 4, 5, 10, 20, 25, 50, 100]
97 的因數: [1, 97]
  → 97 是質數'''
    },
    8: {  # ★★★ 字串加密
        "code": '''def encrypt(text):
    return "".join(chr(ord(c) + 1) for c in text)

def decrypt(text):
    return "".join(chr(ord(c) - 1) for c in text)

original = "Hello World"
encrypted = encrypt(original)
decrypted = decrypt(encrypted)

print(f"原文: {original}")
print(f"加密: {encrypted}")
print(f"解密: {decrypted}")''',
        "output": '''原文: Hello World
加密: Ifmmp!Xpsme
解密: Hello World'''
    },
    9: {  # ★★★ 學生成績系統
        "code": '''students = []

def add_student(name, score):
    students.append({"name": name, "score": score})

def find_student(name):
    for s in students:
        if s["name"] == name:
            return s
    return None

def class_average():
    if not students:
        return 0
    return sum(s["score"] for s in students) / len(students)

add_student("小明", 85)
add_student("小華", 92)
add_student("小美", 78)

print("=== 學生成績 ===")
for s in students:
    print(f"  {s['name']}: {s['score']}")

print(f"\\n查詢小華: {find_student('小華')}")
print(f"班級平均: {class_average():.1f}")''',
        "output": '''=== 學生成績 ===
  小明: 85
  小華: 92
  小美: 78

查詢小華: {'name': '小華', 'score': 92}
班級平均: 85.0'''
    },
    10: {  # ★★★★ 倒三角形
        "code": '''def inverted_triangle(width):
    for i in range(width, 0, -2):
        spaces = " " * ((width - i) // 2)
        stars = "*" * i
        print(spaces + stars)

inverted_triangle(9)''',
        "output": '''*********
 *******
  *****
   ***
    *'''
    },
    11: {  # ★★★★ 字元統計
        "code": '''text = "Hello World! 123"

upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())
digit = sum(1 for c in text if c.isdigit())
space = sum(1 for c in text if c.isspace())
special = len(text) - upper - lower - digit - space

print(f"字串: '{text}'")
print(f"大寫: {upper}")
print(f"小寫: {lower}")
print(f"數字: {digit}")
print(f"空格: {space}")
print(f"特殊符號: {special}")''',
        "output": '''字串: 'Hello World! 123'
大寫: 2
小寫: 8
數字: 3
空格: 2
特殊符號: 1'''
    },
    12: {  # ★★★★ 矩陣運算
        "code": '''A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# 矩陣加法
def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# 矩陣轉置
def matrix_transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

print("矩陣 A:")
for row in A:
    print(f"  {row}")

print("\\nA + B:")
for row in matrix_add(A, B):
    print(f"  {row}")

print("\\nA 轉置:")
for row in matrix_transpose(A):
    print(f"  {row}")''',
        "output": '''矩陣 A:
  [1, 2, 3]
  [4, 5, 6]
  [7, 8, 9]

A + B:
  [10, 10, 10]
  [10, 10, 10]
  [10, 10, 10]

A 轉置:
  [1, 4, 7]
  [2, 5, 8]
  [3, 6, 9]'''
    },
    13: {  # ★★★★★ 快速排序
        "code": '''def quicksort(arr, depth=0):
    indent = "  " * depth
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print(f"{indent}pivot={pivot}: L{left} M{middle} R{right}")

    return quicksort(left, depth+1) + middle + quicksort(right, depth+1)

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"原始: {arr}")
print("\\n排序過程:")
result = quicksort(arr)
print(f"\\n結果: {result}")''',
        "output": '''原始: [64, 34, 25, 12, 22, 11, 90]

排序過程:
pivot=12: L[11] M[12] R[64, 34, 25, 22, 90]
  pivot=25: L[22] M[25] R[64, 34, 90]
    pivot=34: L[] M[34] R[64, 90]
      pivot=90: L[64] M[90] R[]

結果: [11, 12, 22, 25, 34, 64, 90]'''
    },
    14: {  # ★★★★★ 括號配對
        "code": '''def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

tests = ["()", "([{}])", "([)]", "{[}", "((()))", ""][:-1]
tests = ["()", "([{}])", "([)]", "{[}", "((()])"]
for t in tests:
    result = "配對正確" if is_balanced(t) else "配對錯誤"
    print(f"'{t}' → {result}")''',
        "output": ''''()' → 配對正確
'([{}])' → 配對正確
'([)]' → 配對錯誤
'{[}' → 配對錯誤
'((())])' → 配對錯誤'''
    },
    15: {  # ★★★★★ LRU 快取
        "code": '''class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            print(f"GET {key}: {self.cache[key]} (命中)")
            return self.cache[key]
        print(f"GET {key}: None (未命中)")
        return None

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.order.pop(0)
            del self.cache[oldest]
            print(f"移除最舊: {oldest}")
        self.cache[key] = value
        self.order.append(key)
        print(f"PUT {key}={value}, 順序: {self.order}")

cache = LRUCache(3)
cache.put("A", 1)
cache.put("B", 2)
cache.put("C", 3)
cache.get("A")
cache.put("D", 4)
cache.get("B")''',
        "output": '''PUT A=1, 順序: ['A']
PUT B=2, 順序: ['A', 'B']
PUT C=3, 順序: ['A', 'B', 'C']
GET A: 1 (命中)
移除最舊: B
PUT D=4, 順序: ['C', 'A', 'D']
GET B: None (未命中)'''
    },
    16: {  # ★★★★★★ 八皇后問題
        "code": '''def solve_queens(n=8):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \\
               board[i] - i == col - row or \\
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == n:
            return True
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                if solve(board, row + 1):
                    return True
        return False

    board = [-1] * n
    solve(board, 0)
    return board

board = solve_queens()
print("=== 八皇后解法 ===")
for i, col in enumerate(board):
    row = ['.'] * 8
    row[col] = 'Q'
    print(' '.join(row))''',
        "output": '''=== 八皇后解法 ===
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .'''
    },
    17: {  # ★★★★★★ 溫室控制類別
        "code": '''class Greenhouse:
    def __init__(self, name):
        self.name = name
        self.temp = 25.0
        self.humidity = 60.0
        self.temp_range = (18, 30)
        self.humidity_range = (50, 80)

    def update(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity
        self.check_alerts()

    def check_alerts(self):
        alerts = []
        if self.temp < self.temp_range[0]:
            alerts.append("溫度過低！啟動加熱")
        elif self.temp > self.temp_range[1]:
            alerts.append("溫度過高！啟動降溫")
        if self.humidity < self.humidity_range[0]:
            alerts.append("濕度過低！啟動加濕")
        elif self.humidity > self.humidity_range[1]:
            alerts.append("濕度過高！啟動除濕")
        for alert in alerts:
            print(f"  ⚠️ {alert}")
        if not alerts:
            print("  ✓ 環境正常")

    def status(self):
        print(f"=== {self.name} ===")
        print(f"溫度: {self.temp}°C")
        print(f"濕度: {self.humidity}%")

gh = Greenhouse("A區溫室")
gh.status()
gh.update(35, 45)
gh.status()''',
        "output": '''=== A區溫室 ===
溫度: 25.0°C
濕度: 60.0%
  ✓ 環境正常
=== A區溫室 ===
溫度: 35°C
濕度: 45%
  ⚠️ 溫度過高！啟動降溫
  ⚠️ 濕度過低！啟動加濕'''
    },
    18: {  # ★★★★★★ 表達式計算機
        "code": '''def evaluate(expr):
    def parse_number(s, i):
        j = i
        while j < len(s) and (s[j].isdigit() or s[j] == '.'):
            j += 1
        return float(s[i:j]), j

    def parse_factor(s, i):
        if s[i] == '(':
            val, i = parse_expr(s, i + 1)
            return val, i + 1  # skip ')'
        return parse_number(s, i)

    def parse_term(s, i):
        val, i = parse_factor(s, i)
        while i < len(s) and s[i] in '*/':
            op = s[i]
            right, i = parse_factor(s, i + 1)
            val = val * right if op == '*' else val / right
        return val, i

    def parse_expr(s, i):
        val, i = parse_term(s, i)
        while i < len(s) and s[i] in '+-':
            op = s[i]
            right, i = parse_term(s, i + 1)
            val = val + right if op == '+' else val - right
        return val, i

    expr = expr.replace(' ', '')
    result, _ = parse_expr(expr, 0)
    return result

tests = ["3+4*2", "(3+4)*2", "10/(2+3)", "2*3+4*5"]
for expr in tests:
    print(f"{expr} = {evaluate(expr)}")''',
        "output": '''3+4*2 = 11.0
(3+4)*2 = 14.0
10/(2+3) = 2.0
2*3+4*5 = 26.0'''
    }
}
