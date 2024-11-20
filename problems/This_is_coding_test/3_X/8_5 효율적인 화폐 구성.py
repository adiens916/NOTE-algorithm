from collections import deque


N, M = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# XXX: 범위는 상수 값으로 정하기. 동적으로 하려면 복잡해져서 실수함.
INF = int(1e9)
table = [INF] * 10001

# 기본 동전들은 1개씩으로 만들 수 있음
for coin in coins:
    table[coin] = 1

# 기본 동전들 갖고 계속 늘려 나가기
queue = deque(coins[:])
while queue:
    # 이전 값 가져오기
    prev = queue.popleft()
    
    for coin in coins:
        # 새로운 값이 목표치 넘어서면 스킵
        if prev + coin > M:
            continue

        # XXX: table[coin]이 아니라 table[prev]에서 1 더해야 함.
        new_count = table[prev] + 1
        # 이전에 만든 값과, 새로 만든 값 비교
        table[prev + coin] = min(table[prev + coin], new_count)

        # 새로 만든 값을 기반으로 또 늘려 나가기
        queue.append(prev + coin)

if table[M] == INF:
    print(-1)
else:
    print(table[M])

"""
2 15
2
3
"""  # 5
"""
3 4
3
5
7
"""  # -1
