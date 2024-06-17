N = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)

MAX = 1000000
for i in range(1, MAX + 1):
    remains = i

    for coin in coins:
        if coin > remains:
            continue
        remains -= coin

    if remains != 0:
        print(i)
        break

"""
5
3 2 1 1 9
"""  # 8
"""
3
3 5 7
"""  # 1
