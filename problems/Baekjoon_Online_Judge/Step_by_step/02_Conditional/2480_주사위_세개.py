"""https://www.acmicpc.net/problem/2480"""

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


dice = list(map(int, input().split()))
count = [0] * 7

for idx in dice:
    count[idx] += 1

max_idx = -1
for idx in range(6, 0, -1):
    if count[idx] == 3:
        prize = 10000 + idx * 1000
        break
    elif count[idx] == 2:
        prize = 1000 + idx * 100
        break
    elif count[idx] == 1:
        max_idx = max(max_idx, idx)
else:
    prize = max_idx * 100

print(prize)