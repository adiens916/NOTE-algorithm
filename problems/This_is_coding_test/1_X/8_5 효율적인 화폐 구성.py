N, M = map(int, input().split())
coin_types = [int(input()) for _ in range(N)]
coin_types.sort()

min_coin_nums = [0] * (M + 1)

for target in range(min(coin_types), M + 1):
    min_standard = M

    for coin in coin_types:
        if coin == target:
            min_coin_nums[target] = 1
            min_standard = M
            break

        if min_coin_nums[target - coin] > 0:
            cur_min = min_coin_nums[target - coin] + 1
            min_standard = min(min_standard, cur_min)

    if min_standard != M:
        min_coin_nums[target] = min_standard

if min_coin_nums[M] == 0:
    min_coin_nums[M] = -1

print(min_coin_nums[M])

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

"""
3 8
1
4
5
"""  # 2
