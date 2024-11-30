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


from collections import deque

def get_edges_bfs(graph: list[list[int]]) -> list[tuple[int, int, int]]:
    # 인접 행렬 기준

    N = len(graph)
    visited = [False] * N
    queue = deque()

    start = 1
    visited[start] = True
    queue.append(start)

    result = []

    while queue:
        start = queue.popleft()

        for i in range(N):
            if visited[i]:
                continue

            edge = graph[start][i]
            if edge > 0:
                # XXX: 행렬이라 연결되지 않은 것도 검색 필요.
                # 연결되어 있어야만 방문 설정하기
                visited[i] = True
                result.append((edge, start, i))
                queue.append(i)

    return result


def kruskal(graph: list[list[int]]) -> int:
    parents = [i for i in range(len(graph))]
    edge_sum = 0

    edges = get_edges_bfs(graph)
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
