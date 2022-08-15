import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


def factorial(N: int):
    if N <= 1:
        return 1
    else:
        return N * factorial(N - 1)


N = int(input())
print(factorial(N))
