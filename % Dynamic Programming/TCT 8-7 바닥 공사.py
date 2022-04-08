"""
DP 테이블 각각에 나머지 값을 넣어도 됨?
"""

N = int(input())

dp_table = [0] * (N + 1)
dp_table[0] = 1
dp_table[1] = 1
for i in range(2, N + 1):
    dp_table[i] = (dp_table[i - 1] + dp_table[i - 2] * 2) # % 796796

print(dp_table[N])
