from pathlib import Path

input_file = Path(__file__).with_suffix(".txt")

import sys

# sys.stdin = open(input_file)
input = sys.stdin.readline


N = int(input())

count = 0
num = 0
while count < N:
    num += 1
    if "666" in str(num):
        count += 1

print(num)
