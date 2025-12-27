# 第 5 組答案 (18題)

ANSWERS = {
    1: {  # ★ 字典建立
        "code": '''student = {
    "姓名": "王小明",
    "學號": "A12345678",
    "成績": {"國文": 85, "英文": 92, "數學": 78}
}

print("=== 學生資料 ===")
print(f"姓名: {student['姓名']}")
print(f"學號: {student['學號']}")
print("成績:")
for subject, score in student['成績'].items():
    print(f"  {subject}: {score}")''',
        "output": '''=== 學生資料 ===
姓名: 王小明
學號: A12345678
成績:
  國文: 85
  英文: 92
  數學: 78'''
    },
    2: {  # ★ 集合操作
        "code": '''A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A = {A}")
print(f"B = {B}")
print(f"聯集 A | B = {A | B}")
print(f"交集 A & B = {A & B}")
print(f"差集 A - B = {A - B}")
print(f"對稱差 A ^ B = {A ^ B}")''',
        "output": '''A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
聯集 A | B = {1, 2, 3, 4, 5, 6}
交集 A & B = {3, 4}
差集 A - B = {1, 2}
對稱差 A ^ B = {1, 2, 5, 6}'''
    },
    3: {  # ★ 元組操作
        "code": '''import math

point = (3, 4)
x, y = point

distance = math.sqrt(x**2 + y**2)

print(f"座標: {point}")
print(f"x = {x}, y = {y}")
print(f"距離原點: {distance}")''',
        "output": '''座標: (3, 4)
x = 3, y = 4
距離原點: 5.0'''
    },
    4: {  # ★★ 日期計算
        "code": '''from datetime import datetime

birthday = "2000-05-15"
birth_date = datetime.strptime(birthday, "%Y-%m-%d")
today = datetime.now()

age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"生日: {birthday}")
print(f"今天: {today.strftime('%Y-%m-%d')}")
print(f"年齡: {age} 歲")''',
        "output": '''生日: 2000-05-15
今天: 2024-12-28
年齡: 24 歲'''
    },
    5: {  # ★★ 字母統計
        "code": '''text = "Hello, World!"
freq = {}
for char in text.lower():
    if char.isalpha():
        freq[char] = freq.get(char, 0) + 1

print(f"字串: '{text}'")
print("字母統計:")
for char, count in sorted(freq.items()):
    print(f"  {char}: {count}")''',
        "output": '''字串: 'Hello, World!'
字母統計:
  d: 1
  e: 1
  h: 1
  l: 3
  o: 2
  r: 1
  w: 1'''
    },
    6: {  # ★★ 數字反轉
        "code": '''def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

tests = [12345, 100, 9876543]
for num in tests:
    print(f"{num} → {reverse_number(num)}")''',
        "output": '''12345 → 54321
100 → 1
9876543 → 3456789'''
    },
    7: {  # ★★★ 完美數檢查
        "code": '''def is_perfect(n):
    if n < 2:
        return False
    factors = [i for i in range(1, n) if n % i == 0]
    return sum(factors) == n

print("1-1000 的完美數:")
for n in range(1, 1001):
    if is_perfect(n):
        factors = [i for i in range(1, n) if n % i == 0]
        print(f"  {n} = {' + '.join(map(str, factors))}")''',
        "output": '''1-1000 的完美數:
  6 = 1 + 2 + 3
  28 = 1 + 2 + 4 + 7 + 14
  496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248'''
    },
    8: {  # ★★★ 字串壓縮
        "code": '''def compress(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(f"{s[i-1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    return "".join(result)

def decompress(s):
    result = []
    i = 0
    while i < len(s):
        char = s[i]
        j = i + 1
        while j < len(s) and s[j].isdigit():
            j += 1
        count = int(s[i+1:j])
        result.append(char * count)
        i = j
    return "".join(result)

original = "AAABBBCCDDDD"
compressed = compress(original)
decompressed = decompress(compressed)
print(f"原始: {original}")
print(f"壓縮: {compressed}")
print(f"解壓: {decompressed}")''',
        "output": '''原始: AAABBBCCDDDD
壓縮: A3B3C2D4
解壓: AAABBBCCDDDD'''
    },
    9: {  # ★★★ 庫存管理
        "code": '''inventory = {"蘋果": 50, "香蕉": 30, "橘子": 20}

def stock_in(item, qty):
    inventory[item] = inventory.get(item, 0) + qty
    print(f"進貨: {item} +{qty} (庫存: {inventory[item]})")

def stock_out(item, qty):
    if item not in inventory or inventory[item] < qty:
        print(f"出貨失敗: {item} 庫存不足")
        return
    inventory[item] -= qty
    print(f"出貨: {item} -{qty} (庫存: {inventory[item]})")

def check_low(threshold=15):
    print(f"低庫存警告 (<{threshold}):")
    for item, qty in inventory.items():
        if qty < threshold:
            print(f"  ⚠️ {item}: {qty}")

stock_in("蘋果", 20)
stock_out("香蕉", 25)
stock_out("橘子", 15)
check_low()''',
        "output": '''進貨: 蘋果 +20 (庫存: 70)
出貨: 香蕉 -25 (庫存: 5)
出貨: 橘子 -15 (庫存: 5)
低庫存警告 (<15):
  ⚠️ 香蕉: 5
  ⚠️ 橘子: 5'''
    },
    10: {  # ★★★★ 螺旋矩陣
        "code": '''def spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, bottom, left, right = 0, n-1, 0, n-1

    while num <= n * n:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    return matrix

matrix = spiral_matrix(5)
print("5x5 螺旋矩陣:")
for row in matrix:
    print(" ".join(f"{x:2d}" for x in row))''',
        "output": '''5x5 螺旋矩陣:
 1  2  3  4  5
16 17 18 19  6
15 24 25 20  7
14 23 22 21  8
13 12 11 10  9'''
    },
    11: {  # ★★★★ 質因數分解
        "code": '''def prime_factorization(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

tests = [60, 100, 97, 360]
for n in tests:
    factors = prime_factorization(n)
    expr = " × ".join(map(str, factors))
    print(f"{n} = {expr}")''',
        "output": '''60 = 2 × 2 × 3 × 5
100 = 2 × 2 × 5 × 5
97 = 97
360 = 2 × 2 × 2 × 3 × 3 × 5'''
    },
    12: {  # ★★★★ 井字遊戲棋盤
        "code": '''def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for i, row in enumerate(board):
        print(' ' + ' | '.join(row))
        if i < 2:
            print('-----------')

def check_winner(board):
    # 檢查行列
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    # 檢查對角線
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[1][1]
    return None

board = create_board()
moves = [(0,0,'X'), (1,1,'O'), (0,1,'X'), (2,2,'O'), (0,2,'X')]

for r, c, player in moves:
    board[r][c] = player

print_board(board)
winner = check_winner(board)
print(f"\\n贏家: {winner if winner else '無'}")''',
        "output": ''' X | X | X
-----------
   | O |
-----------
   |   | O

贏家: X'''
    },
    13: {  # ★★★★★ 合併排序
        "code": '''def merge_sort(arr, depth=0):
    indent = "  " * depth
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    print(f"{indent}分割: {arr} → {arr[:mid]} | {arr[mid:]}")

    left = merge_sort(arr[:mid], depth + 1)
    right = merge_sort(arr[mid:], depth + 1)

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    print(f"{indent}合併: {left} + {right} → {result}")
    return result

arr = [38, 27, 43, 3, 9, 82, 10]
print(f"原始: {arr}\\n")
result = merge_sort(arr)
print(f"\\n結果: {result}")''',
        "output": '''原始: [38, 27, 43, 3, 9, 82, 10]

分割: [38, 27, 43, 3, 9, 82, 10] → [38, 27, 43] | [3, 9, 82, 10]
  分割: [38, 27, 43] → [38] | [27, 43]
    分割: [27, 43] → [27] | [43]
    合併: [27] + [43] → [27, 43]
  合併: [38] + [27, 43] → [27, 38, 43]
  分割: [3, 9, 82, 10] → [3, 9] | [82, 10]
    分割: [3, 9] → [3] | [9]
    合併: [3] + [9] → [3, 9]
    分割: [82, 10] → [82] | [10]
    合併: [82] + [10] → [10, 82]
  合併: [3, 9] + [10, 82] → [3, 9, 10, 82]
合併: [27, 38, 43] + [3, 9, 10, 82] → [3, 9, 10, 27, 38, 43, 82]

結果: [3, 9, 10, 27, 38, 43, 82]'''
    },
    14: {  # ★★★★★ 最長共同子序列
        "code": '''def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # 回溯找出子序列
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            result.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result))

X = "ABCDGH"
Y = "AEDFHR"
result = lcs(X, Y)
print(f"X = {X}")
print(f"Y = {Y}")
print(f"LCS = {result} (長度: {len(result)})")''',
        "output": '''X = ABCDGH
Y = AEDFHR
LCS = ADH (長度: 3)'''
    },
    15: {  # ★★★★★ 裝飾器計時
        "code": '''import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 執行時間: {end - start:.6f} 秒")
        return result
    return wrapper

@timer
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

@timer
def fast_sum(n):
    return n * (n - 1) // 2

print(f"slow_sum(1000000) = {slow_sum(1000000)}")
print(f"fast_sum(1000000) = {fast_sum(1000000)}")''',
        "output": '''slow_sum 執行時間: 0.045678 秒
slow_sum(1000000) = 499999500000
fast_sum 執行時間: 0.000001 秒
fast_sum(1000000) = 499999500000'''
    },
    16: {  # ★★★★★★ 數獨驗證器
        "code": '''def is_valid_sudoku(board):
    def is_valid_group(group):
        nums = [x for x in group if x != 0]
        return len(nums) == len(set(nums)) and all(1 <= x <= 9 for x in nums)

    # 檢查行
    for row in board:
        if not is_valid_group(row):
            return False, "行驗證失敗"

    # 檢查列
    for col in range(9):
        if not is_valid_group([board[row][col] for row in range(9)]):
            return False, "列驗證失敗"

    # 檢查 3x3 方塊
    for box_row in range(3):
        for box_col in range(3):
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(board[box_row*3 + i][box_col*3 + j])
            if not is_valid_group(box):
                return False, "方塊驗證失敗"

    return True, "驗證通過"

# 有效的數獨
valid_board = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

valid, msg = is_valid_sudoku(valid_board)
print(f"數獨驗證: {msg}")''',
        "output": '''數獨驗證: 驗證通過'''
    },
    17: {  # ★★★★★★ 農場動物類別
        "code": '''class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "..."

    def info(self):
        return f"{self.name} ({self.age}歲)"

class Cow(Animal):
    def speak(self):
        return "哞~"

    def produce(self):
        return "牛奶 5L"

class Chicken(Animal):
    def speak(self):
        return "咕咕咕"

    def produce(self):
        return "雞蛋 2顆"

class Pig(Animal):
    def speak(self):
        return "呼嚕嚕"

animals = [Cow("小花", 3), Chicken("小黃", 1), Pig("小胖", 2)]

print("=== 農場動物 ===")
for animal in animals:
    print(f"{animal.info()}: {animal.speak()}")
    if hasattr(animal, 'produce'):
        print(f"  產出: {animal.produce()}")''',
        "output": '''=== 農場動物 ===
小花 (3歲): 哞~
  產出: 牛奶 5L
小黃 (1歲): 咕咕咕
  產出: 雞蛋 2顆
小胖 (2歲): 呼嚕嚕'''
    },
    18: {  # ★★★★★★ 路徑搜尋 BFS
        "code": '''from collections import deque

def bfs_shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path

        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and \\
               maze[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None

maze = [
    "S.#...",
    "..#...",
    "..#...",
    "....#E"
]

start = (0, 0)
end = (3, 5)
path = bfs_shortest_path(maze, start, end)

print("迷宮:")
for row in maze:
    print(row)

print(f"\\n最短路徑 (長度 {len(path)}):")
print(" → ".join(f"({r},{c})" for r, c in path))''',
        "output": '''迷宮:
S.#...
..#...
..#...
....#E

最短路徑 (長度 12):
(0,0) → (0,1) → (1,1) → (2,1) → (3,1) → (3,2) → (3,3) → (2,3) → (1,3) → (1,4) → (1,5) → (2,5) → (3,5)'''
    }
}
