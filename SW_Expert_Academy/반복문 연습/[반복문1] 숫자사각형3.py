
from pathlib import Path
import os
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case}")

    H, W = map(int, input().split())
    for row in range(H):
        if row % 2 == 0:
            for col in range(W):
                print(row * W + 1 + col, end=' ')
        else:
            for col in range(W):
                print((row + 1) * W - col, end=' ')
        print()