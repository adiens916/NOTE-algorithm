import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


cur_max = 0
cur_idx = 0

for i in range(1, 10):
    n = int(input())
    if n > cur_max:
        cur_max = n
        cur_idx = i

print(cur_max, cur_idx, sep='\n')