
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
    numbers = list(map(int, input().split()))

    min_num = 1000001
    max_num = 0

    for i in range(N):
        min_num = numbers[i] if numbers[i] < min_num else min_num
        max_num = numbers[i] if numbers[i] > max_num else max_num
    
    print("#{} {}".format(test_case, max_num - min_num))
