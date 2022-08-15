from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
n, m 크기가 크다 => 수학 문제
FIXME: 메모리 문제 => 리스트 X => 변수로만
"""

N, M = map(int, input().split())

# DP 방식으로 팩토리얼 구하기
fact = 1
for i in range(2, N + 1):
    fact *= i
    
    if i == N:
        fact_n = fact
    elif i == N - M:
        fact_n_m = fact
    elif i == M:
        fact_m = fact

# 식 써서 조합 구하기
nCm = fact_n // (fact_n_m * fact_m)

# 문자열로 만들어서, 뒤에서부터 0 개수 세기
nCm = str(nCm)
zero_count = 0
for i in range(len(nCm) - 1, -1, -1):
    if nCm[i] == '0':
        zero_count += 1
    else:
        break

print(zero_count)
