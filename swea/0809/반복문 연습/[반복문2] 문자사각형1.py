
from pathlib import Path
import os
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


a = ord('A')
cycle = ord('Z') - ord('A') + 1

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case}")

    N = int(input())
    for row in range(1, N + 1):
        for col in range(N):
            print(chr((N ** 2 - row - N * col) % cycle + a), end=' ')
        print()