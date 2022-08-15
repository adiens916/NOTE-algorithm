N, M = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# 계산된 결과를 저장하기 위한 DP 테이블 초기화
memo = [10001] * (M + 1)

# DP 진행 (바텀-업)
memo[0] = 0

for coin in coins:
    for i in range(coin, M + 1):
        # i - k 원을 만드는 방법이 존재하는 경우
        if memo[i - coin] != 10001:
            memo[i] = min(memo[i], memo[i - coin] + 1)

if memo[M] == 10001:
    print(-1)
else:
    print(memo[M])