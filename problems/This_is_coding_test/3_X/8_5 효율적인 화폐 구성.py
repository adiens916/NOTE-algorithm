N, M = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# XXX: 코인 최대치까지 만들...려고 했으나, 더하면 최대치 넘어섬. 최대치의 2배로 만들기
# XXX: 목표 값 / 코인 값 중 더 큰 것 기준으로 만드...는 건 메모리 낭비가 심함.
MAX = max(max(coins), M)
table = [0] * (2 * MAX + 1)
# 기본 동전들은 1개씩으로 만들 수 있음
for coin in coins:
    table[coin] = 1

# 기본 동전들 갖고 계속 늘려 나가기
stack = coins[:]
while stack:
    # 이전 값 가져오기
    prev = stack.pop()
    
    for coin in coins:
        # 새로운 값이 목표치 넘어서면 스킵
        if prev + coin > M:
            continue

        # XXX: 효율성을 위해, 이미 계산된 건 중복 계산이므로 스킵
        if table[prev + coin] > 0:
            continue

        # XXX: table[coin]이 아니라 table[prev]에서 1 더해야 함.
        new_count = table[prev] + 1
        # 이전에 계산한 적 없으면, 이전 개수에서 1개 더하면 만들 수 있음.
        if table[prev + coin] == 0:
            table[prev + coin] = new_count
        # 이전에 계산한 적 있으면, 개수 비교
        else:
            table[prev + coin] = min(table[prev + coin], new_count)

        # 새로 만든 값을 기반으로 또 늘려 나가기
        stack.append(prev + coin)

if table[M] == 0:
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
