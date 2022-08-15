"""https://www.acmicpc.net/problem/10926"""

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


dup_id = input().strip()
print(dup_id + '??!')