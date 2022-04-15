import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


T = int(input())
for case in range(1, T + 1):
    A, B = map(int, input().split())
    print(f'Case #{case}: {A} + {B} = {A + B}')
