import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


N = int(input())
arr = [int(input()) for _ in range(N)]
print(*sorted(arr), sep='\n')
