# 第 6 組答案 (18題)

ANSWERS = {
    1: {  # ★ 迴圈練習
        "code": '''print("1-100 中 3 或 5 的倍數:")
multiples = [i for i in range(1, 101) if i % 3 == 0 or i % 5 == 0]
print(multiples)
print(f"共 {len(multiples)} 個")''',
        "output": '''1-100 中 3 或 5 的倍數:
[3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50, 51, 54, 55, 57, 60, 63, 65, 66, 69, 70, 72, 75, 78, 80, 81, 84, 85, 87, 90, 93, 95, 96, 99, 100]
共 47 個'''
    },
    2: {  # ★ 字串格式化
        "code": '''name = "小明"
age = 18
score = 95.5

# % 運算子
print("方法1: %s 今年 %d 歲，得分 %.1f" % (name, age, score))

# format()
print("方法2: {} 今年 {} 歲，得分 {:.1f}".format(name, age, score))

# f-string
print(f"方法3: {name} 今年 {age} 歲，得分 {score:.1f}")''',
        "output": '''方法1: 小明 今年 18 歲，得分 95.5
方法2: 小明 今年 18 歲，得分 95.5
方法3: 小明 今年 18 歲，得分 95.5'''
    },
    3: {  # ★ 列表生成式
        "code": '''squares = [x**2 for x in range(1, 11)]
print(f"1-10 的平方數: {squares}")

# 其他列表生成式範例
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"1-20 偶數: {evens}")

pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(f"座標對: {pairs}")''',
        "output": '''1-10 的平方數: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
1-20 偶數: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
座標對: [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]'''
    },
    4: {  # ★★ 質數檢查
        "code": '''def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

tests = [2, 17, 21, 97, 100]
for n in tests:
    result = "是質數" if is_prime(n) else "不是質數"
    print(f"{n}: {result}")''',
        "output": '''2: 是質數
17: 是質數
21: 不是質數
97: 是質數
100: 不是質數'''
    },
    5: {  # ★★ 字串處理
        "code": '''import string

text = "Hello, World! 123 - Python Programming"

# 只保留字母和數字
result = "".join(c for c in text if c.isalnum())
print(f"原始: '{text}'")
print(f"處理後: '{result}'")''',
        "output": '''原始: 'Hello, World! 123 - Python Programming'
處理後: 'HelloWorld123PythonProgramming'''
    },
    6: {  # ★★ 階乘計算
        "code": '''# 迴圈方式
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 遞迴方式
def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)

n = 10
print(f"{n}! (迴圈) = {factorial_loop(n)}")
print(f"{n}! (遞迴) = {factorial_rec(n)}")''',
        "output": '''10! (迴圈) = 3628800
10! (遞迴) = 3628800'''
    },
    7: {  # ★★★ 二進位轉換
        "code": '''def to_binary(n):
    if n == 0:
        return "0"
    result = ""
    print(f"轉換 {n} 為二進位:")
    original = n
    while n > 0:
        remainder = n % 2
        print(f"  {n} ÷ 2 = {n//2} 餘 {remainder}")
        result = str(remainder) + result
        n //= 2
    return result

num = 42
binary = to_binary(num)
print(f"\\n結果: {num} = {binary}")
print(f"驗證: int('{binary}', 2) = {int(binary, 2)}")''',
        "output": '''轉換 42 為二進位:
  42 ÷ 2 = 21 餘 0
  21 ÷ 2 = 10 餘 1
  10 ÷ 2 = 5 餘 0
  5 ÷ 2 = 2 餘 1
  2 ÷ 2 = 1 餘 0
  1 ÷ 2 = 0 餘 1

結果: 42 = 101010
驗證: int('101010', 2) = 42'''
    },
    8: {  # ★★★ 沙漏圖案
        "code": '''def draw_hourglass(size):
    # 上半部 (倒三角)
    for i in range(size, 0, -1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
    # 下半部 (正三角)
    for i in range(2, size + 1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

draw_hourglass(5)''',
        "output": '''*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********'''
    },
    9: {  # ★★★ 成績管理字典
        "code": '''grades = {
    "一年甲班": {"小明": 85, "小華": 92, "小美": 78},
    "一年乙班": {"小強": 88, "小麗": 95, "小志": 72}
}

def class_average(class_name):
    scores = grades[class_name].values()
    return sum(scores) / len(scores)

def student_score(class_name, name):
    return grades.get(class_name, {}).get(name, None)

print("=== 成績管理 ===")
for cls in grades:
    print(f"\\n{cls}:")
    for name, score in grades[cls].items():
        print(f"  {name}: {score}")
    print(f"  班級平均: {class_average(cls):.1f}")

print(f"\\n查詢一年甲班小明: {student_score('一年甲班', '小明')}")''',
        "output": '''=== 成績管理 ===

一年甲班:
  小明: 85
  小華: 92
  小美: 78
  班級平均: 85.0

一年乙班:
  小強: 88
  小麗: 95
  小志: 72
  班級平均: 85.0

查詢一年甲班小明: 85'''
    },
    10: {  # ★★★★ 矩陣乘法
        "code": '''def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        return None

    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = [[1, 2, 3], [4, 5, 6]]  # 2x3
B = [[7, 8], [9, 10], [11, 12]]  # 3x2

print("A (2x3):")
for row in A:
    print(f"  {row}")

print("\\nB (3x2):")
for row in B:
    print(f"  {row}")

C = matrix_multiply(A, B)
print("\\nA × B (2x2):")
for row in C:
    print(f"  {row}")''',
        "output": '''A (2x3):
  [1, 2, 3]
  [4, 5, 6]

B (3x2):
  [7, 8]
  [9, 10]
  [11, 12]

A × B (2x2):
  [58, 64]
  [139, 154]'''
    },
    11: {  # ★★★★ 最小公倍數
        "code": '''def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_multiple(*args):
    result = args[0]
    for num in args[1:]:
        result = lcm(result, num)
    return result

nums = [12, 18, 24]
print(f"數字: {nums}")
print(f"\\nGCD(12, 18) = {gcd(12, 18)}")
print(f"LCM(12, 18) = {lcm(12, 18)}")
print(f"\\n{nums} 的最小公倍數 = {lcm_multiple(*nums)}")''',
        "output": '''數字: [12, 18, 24]

GCD(12, 18) = 6
LCM(12, 18) = 36

[12, 18, 24] 的最小公倍數 = 72'''
    },
    12: {  # ★★★★ 文字藝術字
        "code": '''DIGITS = {
    '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
    '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
    '2': [" *** ", "*   *", "  ** ", " *   ", "*****"],
    '3': [" *** ", "*   *", "  ** ", "*   *", " *** "],
    '4': ["*   *", "*   *", "*****", "    *", "    *"],
    '5': ["*****", "*    ", "**** ", "    *", "**** "],
    '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
    '7': ["*****", "   * ", "  *  ", " *   ", "*    "],
    '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
    '9': [" *** ", "*   *", " ****", "    *", " *** "]
}

def print_ascii_number(num_str):
    for line in range(5):
        row = ""
        for digit in num_str:
            if digit in DIGITS:
                row += DIGITS[digit][line] + "  "
        print(row)

print("數字 12345:")
print_ascii_number("12345")''',
        "output": '''數字 12345:
  *    ***  *   * *   * *****
 **   *   * *   * *   * *
  *     **  ***** ***** ****
  *    *        *     *     *
 ***  *****     *     * ****'''
    },
    13: {  # ★★★★★ 堆疊計算機
        "code": '''def evaluate_postfix(expr):
    stack = []
    tokens = expr.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
        print(f"  處理 '{token}': 堆疊 = {stack}")

    return stack[0]

expressions = ["3 4 + 2 *", "5 1 2 + 4 * + 3 -"]
for expr in expressions:
    print(f"\\n計算: {expr}")
    result = evaluate_postfix(expr)
    print(f"結果: {result}")''',
        "output": '''
計算: 3 4 + 2 *
  處理 '3': 堆疊 = [3]
  處理 '4': 堆疊 = [3, 4]
  處理 '+': 堆疊 = [7]
  處理 '2': 堆疊 = [7, 2]
  處理 '*': 堆疊 = [14]
結果: 14

計算: 5 1 2 + 4 * + 3 -
  處理 '5': 堆疊 = [5]
  處理 '1': 堆疊 = [5, 1]
  處理 '2': 堆疊 = [5, 1, 2]
  處理 '+': 堆疊 = [5, 3]
  處理 '4': 堆疊 = [5, 3, 4]
  處理 '*': 堆疊 = [5, 12]
  處理 '+': 堆疊 = [17]
  處理 '3': 堆疊 = [17, 3]
  處理 '-': 堆疊 = [14]
結果: 14'''
    },
    14: {  # ★★★★★ 生成器函式
        "code": '''def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 取前 20 項
fib_gen = fibonacci_generator()
fib_list = [next(fib_gen) for _ in range(20)]

print("費氏數列前 20 項 (生成器):")
print(fib_list)

# 另一種使用方式
print("\\n逐一取值:")
gen = fibonacci_generator()
for i in range(5):
    print(f"  F({i}) = {next(gen)}")''',
        "output": '''費氏數列前 20 項 (生成器):
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

逐一取值:
  F(0) = 0
  F(1) = 1
  F(2) = 1
  F(3) = 2
  F(4) = 3'''
    },
    15: {  # ★★★★★ 圖形走訪 DFS
        "code": '''def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph.get(start, []):
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            paths.extend(new_paths)
    return paths

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D', 'E'],
    'D': ['E', 'F'],
    'E': ['F'],
    'F': []
}

print("圖形結構:")
for node, neighbors in graph.items():
    print(f"  {node} → {neighbors}")

paths = find_all_paths(graph, 'A', 'F')
print(f"\\n從 A 到 F 的所有路徑:")
for i, path in enumerate(paths, 1):
    print(f"  {i}. {' → '.join(path)}")''',
        "output": '''圖形結構:
  A → ['B', 'C']
  B → ['C', 'D']
  C → ['D', 'E']
  D → ['E', 'F']
  E → ['F']
  F → []

從 A 到 F 的所有路徑:
  1. A → B → C → D → E → F
  2. A → B → C → D → F
  3. A → B → C → E → F
  4. A → B → D → E → F
  5. A → B → D → F
  6. A → C → D → E → F
  7. A → C → D → F
  8. A → C → E → F'''
    },
    16: {  # ★★★★★★ 貪婪演算法
        "code": '''def make_change(amount, coins):
    coins = sorted(coins, reverse=True)
    result = {}
    remaining = amount

    print(f"找零 ${amount}:")
    for coin in coins:
        if remaining >= coin:
            count = remaining // coin
            result[coin] = count
            remaining -= coin * count
            print(f"  ${coin} x {count} = ${coin * count}")

    return result, remaining

coins = [50, 10, 5, 1]
amount = 167

result, remaining = make_change(amount, coins)
total_coins = sum(result.values())
print(f"\\n總共使用 {total_coins} 枚硬幣")
if remaining > 0:
    print(f"無法找零: ${remaining}")''',
        "output": '''找零 $167:
  $50 x 3 = $150
  $10 x 1 = $10
  $5 x 1 = $5
  $1 x 2 = $2

總共使用 7 枚硬幣'''
    },
    17: {  # ★★★★★★ 感測網路類別
        "code": '''class SensorNetwork:
    def __init__(self, name):
        self.name = name
        self.sensors = {}

    def add_sensor(self, sensor_id, sensor_type):
        self.sensors[sensor_id] = {
            "type": sensor_type,
            "readings": []
        }
        print(f"新增感測器: {sensor_id} ({sensor_type})")

    def add_reading(self, sensor_id, value):
        if sensor_id in self.sensors:
            self.sensors[sensor_id]["readings"].append(value)

    def aggregate(self):
        result = {}
        for sid, data in self.sensors.items():
            if data["readings"]:
                result[sid] = {
                    "avg": sum(data["readings"]) / len(data["readings"]),
                    "max": max(data["readings"]),
                    "min": min(data["readings"])
                }
        return result

    def detect_anomaly(self, threshold=2):
        anomalies = []
        for sid, data in self.sensors.items():
            readings = data["readings"]
            if len(readings) < 2:
                continue
            avg = sum(readings) / len(readings)
            std = (sum((x - avg) ** 2 for x in readings) / len(readings)) ** 0.5
            for r in readings:
                if abs(r - avg) > threshold * std and std > 0:
                    anomalies.append((sid, r))
        return anomalies

network = SensorNetwork("農場A")
network.add_sensor("T1", "溫度")
network.add_sensor("H1", "濕度")

for t in [25, 26, 25, 27, 45, 26]:  # 45 是異常值
    network.add_reading("T1", t)

print(f"\\n聚合資料: {network.aggregate()}")
print(f"異常偵測: {network.detect_anomaly()}")''',
        "output": '''新增感測器: T1 (溫度)
新增感測器: H1 (濕度)

聚合資料: {'T1': {'avg': 29.0, 'max': 45, 'min': 25}}
異常偵測: [('T1', 45)]'''
    },
    18: {  # ★★★★★★ Dijkstra 最短路徑
        "code": '''import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    pq = [(0, start)]

    while pq:
        curr_dist, curr = heapq.heappop(pq)
        if curr_dist > distances[curr]:
            continue
        for neighbor, weight in graph[curr].items():
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = curr
                heapq.heappush(pq, (distance, neighbor))

    # 回溯路徑
    path = []
    node = end
    while node:
        path.append(node)
        node = previous[node]
    path.reverse()

    return distances[end], path

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 8, 'E': 10},
    'D': {'E': 2, 'F': 6},
    'E': {'F': 3},
    'F': {}
}

print("加權圖:")
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        print(f"  {node} --{weight}--> {neighbor}")

dist, path = dijkstra(graph, 'A', 'F')
print(f"\\nA 到 F 最短路徑:")
print(f"  路徑: {' → '.join(path)}")
print(f"  距離: {dist}")''',
        "output": '''加權圖:
  A --4--> B
  A --2--> C
  B --1--> C
  B --5--> D
  C --8--> D
  C --10--> E
  D --2--> E
  D --6--> F
  E --3--> F

A 到 F 最短路徑:
  路徑: A → B → D → E → F
  距離: 14'''
    }
}
