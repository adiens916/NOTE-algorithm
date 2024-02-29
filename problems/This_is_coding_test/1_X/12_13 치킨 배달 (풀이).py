from itertools import combinations

HOUSE = 1
CHICKEN = 2


N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for r in range(N):
    for c in range(N):
        if town[r][c] == CHICKEN:
            chickens.append((r, c))
        elif town[r][c] == HOUSE:
            houses.append((r, c))


def get_length(house: tuple, chicken: tuple) -> int:
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])


# XXX: 치킨들의 조합을 구하기
candidates = combinations(chickens, M)
min_length_sum = 1e9

for candidate_list in candidates:
    cur_length_sum = 0

    for house in houses:
        cur_length = 1e9
        for chicken in candidate_list:
            cur_length = min(cur_length, get_length(house, chicken))

        cur_length_sum += cur_length

    min_length_sum = min(min_length_sum, cur_length_sum)

print(min_length_sum)


"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
"""  # 5
"""
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
"""  # 10
"""
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1 
"""  # 32
