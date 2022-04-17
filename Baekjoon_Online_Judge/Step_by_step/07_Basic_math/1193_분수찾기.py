import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


X = int(input())

# 순서가 대각선 방향으로 증가함.
# 이 지그재그가 첫 행이나 첫 열에 닿을 때의 값
# = 해당 대각선에서 제일 큰 숫자
# 이 값들은 계차수열의 형태를 이룬다. (1, 3, 6, 10, ...)
line_end_index = 0
increment = 0

# 현재 끝 값이 아직 X보다 작은 경우, 좀 더 진행해야 함
while line_end_index < X:
    increment += 1
    line_end_index += increment

# 반복문을 나온 경우, 원하는 순서가 현재 대각선 안에 있음.
# 증분이 짝수면, 최댓값은 첫 열에 있음.
if increment % 2 == 0:
    # 최댓값과 원하는 값 사이의 거리 구하기
    diff = line_end_index - X
    # 해당 거리만큼 가감해서 원하는 위치 구하기
    row = (increment - 1) - diff
    col = diff
else:
    diff = line_end_index - X
    row = diff
    col = (increment - 1) - diff

print(f'{row + 1}/{col + 1}')
