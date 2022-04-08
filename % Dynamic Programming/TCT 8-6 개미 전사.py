"""
초기값은 따로 지정하는 게 더 효율적
"""

N = int(input())
arr = list(map(int, input().split()))

dp_table = [0] * N

# 내가 푼 방식: 전부 if로 나누기
i = 0
while i < N:
    if i > 1:
        # 단 2가지 경우만 존재.
        # i - 1 번째 식량 창고를 털거나
        # i - 2랑 현재 창고를 털거나
        dp_table[i] = max(dp_table[i - 1], dp_table[i - 2] + arr[i])
    elif i == 1:
        dp_table[i] = max(arr[1], arr[0])
    elif i == 0:
        dp_table[i] = arr[0]
    i += 1

# 더 나은 방식: 초기값 따로 지정
dp_table[0] = arr[0]
dp_table[1] = max(arr[0], arr[1])
for i in range(2, N):
    dp_table[i] = max(dp_table[i - 1], dp_table[i - 2] + arr[i])

print(dp_table[N - 1])

"""
4
1 3 1 5
=> 8
"""
