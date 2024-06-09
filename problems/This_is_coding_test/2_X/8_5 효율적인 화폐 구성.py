"""
12 구성하는 경우는

1, 4, 5 동전일 때

5+5+1+1 => 4개
4+4+4 => 3개

동전 개수는 이전 값 + 1
단, 이전 값이 있는 경우에만.
"""


N, M = map(int, input().split())
coin_types = [int(input()) for _ in range(N)]

# XXX: 최솟값 비교할 거니까, 매우 큰 값으로 초기화
INF = int(1e9)
tables = [INF] * 10001
for coin in coin_types:
    tables[coin] = 1

min_coin = min(coin_types)

for i in range(min_coin + 1, M + 1):
    for coin in coin_types:
        prev = i - coin

        # 금액은 자연수여야 함.
        if prev < 1:
            continue

        # 이전 금액까지 만드는 방법 없으면 넘어감
        if tables[prev] == INF:
            continue

        # XXX: 이전 금액까지 만드는 방법에서 1 더한 값 vs. 여태까지의 최소값 비교
        tables[i] = min(tables[i], tables[prev] + 1)

if tables[M] != INF:
    print(tables[M])
else:
    print(-1)

"""
3 4
3
5
7
"""  # -1
"""
3 12
1
4
5
"""  # 3
