"""https://www.acmicpc.net/problem/2775"""

"""
숫자들을 써봤으나 일관된 규칙을 찾기가 어려웠음
현재 결과를 구할 때 이전 결과를 참조하므로 DP로 풀기로 함.
"""

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


# 1. 테이블을 만듦
dp_table = [[0] * 15 for _ in range(15)]
# 2. 종료 조건을 위해 1행을 초기화해줌
for i in range(1, 15):
    dp_table[0][i] = i

# f(k, n) = ∑ f(k - 1, i) (i는 1부터 n까지)
# 이 f를 '함수'로 그대로 치환하면 됨.
def dp(k, n):
    # 테이블이 비어있으면 게산해서 구하기
    if not dp_table[k][n]:
        dp_table[k][n] = sum(
            dp(k - 1, i) for i in range(1, n + 1)
        )
    return dp_table[k][n]


T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp(k, n))
