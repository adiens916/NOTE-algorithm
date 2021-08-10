
from pathlib import Path
import os
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    prefix_sum_max = 0
    prefix_sum_min = N * 10000 + 1

    for base in range(N - M + 1):
        prefix_sum = 0
        for i in range(base, base + M):
            prefix_sum += numbers[i]
        
        if prefix_sum > prefix_sum_max:
            prefix_sum_max = prefix_sum
        if prefix_sum < prefix_sum_min:
            prefix_sum_min = prefix_sum
    
    print("#{} {}".format(test_case, prefix_sum_max - prefix_sum_min))
