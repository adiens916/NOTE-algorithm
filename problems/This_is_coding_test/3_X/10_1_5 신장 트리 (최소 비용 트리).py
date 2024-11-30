def find_parents(x: int, parents: list[int]) -> int:
    if parents[x] != x:
        parents[x] = find_parents(parents[x], parents)
    return parents[x]


def union(a: int, b: int, parents: list[int]) -> None:
    ap = find_parents(a, parents)
    bp = find_parents(b, parents)

    if ap < bp:
        parents[bp] = ap
    else:
        parents[ap] = bp


def get_edges(graph: list[list[int]]) -> list[tuple[int, int, int]]:
    # 인접 행렬 기준
    # XXX: visited가 1차원인 경우, 노드만 중복되지 않게 검사함.
    # 그래서 아직 방문 안 한 간선이 있어도, 이미 방문한 노드는 스킵되어 간선 부족해짐.
    # ⇒ (A) 간선이 중복되지 않아야 하므로 visited는 2차원으로 구현 필요 (인접 리스트에도 유효)
    # ⇒ (B) 인접 행렬이니까 visited 없이 간단하게 우측 상단만 읽어도 됨.

    result = []
    start = 1
    N = len(graph)

    for row in range(start, N):
        for col in range(row + 1, N):
            edge = graph[row][col]
            if edge > 0:
                result.append((edge, row, col))

    return result


def kruskal(graph: list[list[int]]) -> int:
    parents = [i for i in range(len(graph))]
    edge_sum = 0

    edges = get_edges(graph)
    # 굳이 heap 필요 없는 듯. 결국 heap도 정렬을 위한 수단이니까.
    edges.sort()

    for edge, a, b in edges:
        ap = find_parents(a, parents)
        bp = find_parents(b, parents)

        if ap != bp:
            union(ap, bp, parents)
            edge_sum += edge

    return edge_sum


V, E = map(int, input().split())

graph = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A][B] = C
    graph[B][A] = C

answer = kruskal(graph)
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
