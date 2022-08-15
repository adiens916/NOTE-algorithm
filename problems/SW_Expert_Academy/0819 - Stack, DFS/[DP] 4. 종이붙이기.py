from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


cases = [0, 1, 3]

def dp(n):
    if n < 3:
        return cases[n]
    else:
        if n > len(cases):
            dp(n - 1)
        new = cases[n - 1] + cases[n - 2] * 2
        cases.append(new)
        return cases[-1]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = dp(N//10)
    print("#{} {}".format(test_case, result))