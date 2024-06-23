# Kruskal 알고리즘으로 최소 신장 트리 구하기
# 그 후 가장 긴 선분을 지우면 트리 2개로 나뉨.


def find_parent(x, parents) -> int:
    if x != parents[x]:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


def union(a, b, parents):
    a = find_parent(a, parents)
    b = find_parent(b, parents)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N, M = map(int, input().split())

parents = [i for i in range(N + 1)]
queue = []
for _ in range(M):
    A, B, C = map(int, input().split())
    queue.append((C, A, B))

queue.sort()
costs = []
for cost, a, b in queue:
    if find_parent(a, parents) != find_parent(b, parents):
        union(a, b, parents)
        costs.append(cost)

costs.pop()
print(sum(costs))
