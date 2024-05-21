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
# XXX: 정렬하게 되는 경우 원래 행성 번호랑 달라지므로, 행성 번호 저장 필요
arr = []
for i in range(N):
    x, y, z = map(int, input().split())
    arr.append((i, x, y, z))

# 행성 간 거리 구하기
# X, Y, Z축 각각 정렬하는 경우, 각 축마다 가장 가까운 행성끼리 붙어 있음.
# (다음 행성 - 현재 행성) 거리를 구하고, 이걸 모든 축에 대해 반복
# 참고: https://chanhuiseok.github.io/posts/baek-34/
queue = []
for axis in range(1, 4):
    arr.sort(key=lambda p: p[axis])
    for i in range(N - 1):
        cost = arr[i + 1][axis] - arr[i][axis]
        heapq.heappush(queue, (cost, arr[i][0], arr[i + 1][0]))

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
