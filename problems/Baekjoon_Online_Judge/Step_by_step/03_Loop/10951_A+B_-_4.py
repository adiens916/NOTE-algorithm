import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


lines = sys.stdin.readlines()
for line in lines:
    A, B = map(int, line.split())
    print(A + B)
