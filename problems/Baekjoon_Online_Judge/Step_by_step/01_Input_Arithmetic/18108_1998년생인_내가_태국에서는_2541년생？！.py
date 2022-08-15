"""https://www.acmicpc.net/problem/18108"""

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


buddhist_year = int(input())
gap = 2541 - 1998
christian_year = buddhist_year - gap
print(christian_year)