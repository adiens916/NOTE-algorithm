from itertools import combinations


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chickens = []
houses = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            houses.append((r, c))
        elif arr[r][c] == 2:
            chickens.append((r, c))

min_total = int(1e9)
for selection in combinations(chickens, M):
    min_city = 0
    for house in houses:
        min_house = int(1e9)
        for chicken in selection:
            dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            min_house = min(min_house, dist)
        min_city += min_house
    min_total = min(min_total, min_city)

print(min_total)
