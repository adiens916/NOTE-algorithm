from collections import deque


def find_parent(x: int, parents: list[int]) -> int:
    if parents[x] != x:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


def union_parent(a: int, b: int, parents: list[int]) -> None:
    a = find_parent(a, parents)
    b = find_parent(b, parents)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N, M = map(int, input().split())

parents = [i for i in range(N + 1)]

edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
max_len = 1
cost_sum = 0

for cost, A, B in edges:
    A = find_parent(A, parents)
    B = find_parent(B, parents)

    if A != B:
        union_parent(A, B, parents)
        max_len = cost
        cost_sum += cost

print(cost_sum - max_len)

"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""
