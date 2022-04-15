import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


numbers = map(int, sys.stdin.readlines())
num_set = set()

for num in numbers:
    num_set.add(num % 42)

print(len(num_set))