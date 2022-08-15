
from pathlib import Path
import os
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().rstrip()))
    numbers = [0] * 10

    for i in range(N):
        numbers[cards[i]] += 1
    
    max_num = -1
    max_num_count = 0
    for i in range(10):
        if numbers[i] >= max_num_count:
            max_num_count = numbers[i]
            max_num = i

    print("#{} {} {}".format(test_case, max_num, max_num_count))
