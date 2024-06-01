N, M = map(int, input().split())
coin_types = [int(input()) for _ in range(N)]
coin_types.sort()

# XXX: 최솟값을 구하는 문제의 경우, 처음부터 최댓값으로 초기화하면 코드가 훨씬 간결해진다.
INF = 10001
min_coin_nums = [INF] * (M + 1)
min_coin_nums[0] = 0

for target in range(1, M + 1):
    for coin in coin_types:
        if min_coin_nums[target - coin] != INF:
            cur_min = min_coin_nums[target - coin] + 1
            # XXX: 중간에 따로 최댓값을 선언해서 비교하는 부분이 생략되어 훨씬 간결해짐.
            # 이 경우엔, 위에서 미리 INF로 초기화를 했으므로, 바로 비교할 수 있음.
            min_coin_nums[target] = min(min_coin_nums[target], cur_min)

if min_coin_nums[M] == INF:
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
