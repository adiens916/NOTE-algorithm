import heapq


def find_parent(x: int, parents: list[int]) -> int:
    if parents[x] != x:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


def union(a: int, b: int, parents: list[int]) -> None:
    a = find_parent(a, parents)
    b = find_parent(b, parents)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 행성 간 거리 구하기 = O(N^2)
queue = []
for a in range(N - 1):
    for b in range(a + 1, N):
        costs = []
        for i in range(3):
            cost = abs(arr[a][i] - arr[b][i])
            costs.append(cost)
        heapq.heappush(queue, (min(costs), a, b))

# 최소 신장 트리 구하기 (크루스칼 알고리즘)
parents = [i for i in range(N)]
total_cost = 0
while queue:
    cost, a, b = heapq.heappop(queue)
    if find_parent(a, parents) != find_parent(b, parents):
        union(a, b, parents)
        total_cost += cost

print(total_cost)

"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""  # 4
