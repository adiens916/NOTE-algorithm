import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


# 최솟값 & 최댓값 갱신을 위해, 
# 처음에는 범위를 벗어난 값으로 초기화.
x_min = y_min = 1001
x_max = y_max = 0
x_sum = y_sum = 0

for _ in range(3):
    x, y = map(int, input().split())
    
    # 1. 각 좌표의 최솟값과 최댓값 갱신
    if x < x_min: x_min = x
    if x > x_max: x_max = x
    if y < y_min: y_min = y
    if y > y_max: y_max = y
    
    # 2. 각 좌표마다 축을 기준으로 합을 구함
    x_sum += x
    y_sum += y

# 3. 나머지 좌표는 총합에서 빼는 방식으로 구하기
a = x_max - x_min
b = y_max - y_min
print(
    4 * x_min + 2 * a - x_sum,
    4 * y_min + 2 * b - y_sum
)