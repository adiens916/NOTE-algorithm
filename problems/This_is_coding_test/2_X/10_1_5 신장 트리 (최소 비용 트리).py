from collections import deque


def find_parent(x: int, parents: list[int]) -> int:
    if x != parents[x]:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


def union(a: int, b:int, parents: list[int]) -> None:
    a = find_parent(a, parents)
    b = find_parent(b, parents)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def kruskal(edges: list[tuple[int, int, int]], N) -> int:
    parents = [i for i in range(N + 1)]

    edge_sum = 0
    # XXX: 이미 정렬된 상태이므로, deque 안 쓰고 for 반복문 돌면 됨.
    queue = deque(edges)
    while queue:
        e, a, b = queue.popleft()
        if find_parent(a, parents) != find_parent(b, parents):
            union(a, b, parents)
            edge_sum += e

    return edge_sum


V, E = map(int, input().split())

edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
edges.sort()

answer = kruskal(edges, V)
print(answer)


"""
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""  # 159

