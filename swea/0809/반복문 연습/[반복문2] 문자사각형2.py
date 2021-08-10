
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
    for row in range(N):
        for col in range(N):
            # 홀수 열
            if col % 2 == 0:
                c = (col * N + 1 + row - 1) % cycle + a
            # 짝수 열
            else:
                c = ((col + 1) * N - row - 1) % cycle + a
            print(chr(c), end=' ')
        print()