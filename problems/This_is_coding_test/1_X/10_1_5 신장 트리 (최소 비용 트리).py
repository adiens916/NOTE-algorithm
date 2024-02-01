# XXX: 최소 비용 트리가 최단 거리를 의미하지는 않는다.
# 예) A, B, C가 삼각형 모양으로 서로 연결되어 있을 때,
# A-B, B-C로 연결된 경우 이는 최소 비용 트리임.
# 그러나 A에서 C로 갈 때는 B를 거치므로 최단 거리는 아님.

# => 최소 비용을 찾는 크루스칼 알고리즘과,
# 최단 거리를 찾는 플로이드-워셜 알고리즘은 쓰임새가 다름.


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


# XXX: 무방향 그래프이므로, 일차원 리스트면 충분함.
def kruskal_alg(edges: list[tuple[int, int, int]], V: int) -> int:
    edges.sort()
    parents = [i for i in range(V + 1)]
    length_sum = 0

    for cost, a, b in edges:
        A = find_parent(a, parents)
        B = find_parent(b, parents)

        if A != B:
            length_sum += cost
            union_parent(A, B, parents)

    return length_sum


V, E = map(int, input().split())

edges = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

length_sum = kruskal_alg(edges, V)
print(length_sum)

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
