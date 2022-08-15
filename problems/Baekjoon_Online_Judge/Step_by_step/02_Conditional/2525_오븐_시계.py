"""https://www.acmicpc.net/problem/2525"""

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


h, m = list(map(int, input().split()))
t = int(input())

# 1. 오븐구이 시간을 시와 분으로 나누어 분배.
h += t // 60
m += t % 60

# 2. 분이 60분을 넘는 경우, 시 단위를 올림.
if m >= 60:
    h += m // 60
    m %= 60

# 3. 24시를 넘기는 경우, 24로 나누기
h %= 24

print(h, m)
