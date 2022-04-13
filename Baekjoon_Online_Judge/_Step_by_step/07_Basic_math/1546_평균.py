"""
https://www.acmicpc.net/problem/1546
"""


from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


N = int(input())
scores = list(map(int, input().split()))

score_sum = sum(scores)
score_avg = score_sum / len(scores)
score_max = max(scores)

new_avg = score_avg * 100 / score_max
print(new_avg)