import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


N = int(input())
arr = [int(input()) for _ in range(N)]

for i in range(N - 1):
    for j in range(i + 1, N):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(*arr, sep='\n')