import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


A, B, C = [int(input()) for _ in range(3)]
result = str(A * B * C)

count = [0] * 10
for num in result:
    count[int(num)] += 1

for idx in range(10):
    print(count[idx])
