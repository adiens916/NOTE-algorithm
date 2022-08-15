import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


def sum_big_int(long: list, short: list):
    if len(long) < len(short):
        long, short = short, long

    i = len(long) - 1
    j = len(short) - 1
    result = [0] * (i + 2)

    while j >= 0:
        result[i + 1] += int(long[i]) + int(short[j])
        if result[i + 1] > 9:
            result[i + 1] -= 10
            result[i] += 1
        i -= 1
        j -= 1
    
    while i >= 0:
        result[i + 1] += int(long[i])
        if result[i + 1] > 9:
            result[i + 1] -= 10
            result[i] += 1
        i -= 1
    
    if result[0]:
        print(*result, sep='')
    else:
        print(*result[1:], sep='')


A, B = input().split()
sum_big_int(list(A), list(B))