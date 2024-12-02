"""
만들 수 있는 값의 최대 = 이전까지의 만들 수 있는 값의 최대 + 새로운 값
(prev_max = prev_max + coin)

즉, 값의 최대치를 늘려가는 것.

값의 최대치 범위가 계속 이어지려면(연결되려면)
[0, prev_max] + [prev_max + 1, ...]

새로 오는 값은 prev_max + 1보다
작거나 같아야 위 범위가 이어짐.
"""

N = int(input())
coins = list(map(int, input().split()))

coins.sort()
prev_max = 0
for coin in coins:
    if prev_max + 1 >= coin:
        prev_max += coin
    else:
        break

print(prev_max + 1)