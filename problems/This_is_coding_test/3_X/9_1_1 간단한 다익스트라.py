def dijkstra_simple(graph: list[list[int]], start: int) -> list[int]:
    N = len(graph) - 1

    INF = int(1e9)
    table = [INF] * (N + 1)
    table[start] = 0

    visited = [False] * (N + 1)

    # XXX: N개의 정점 개수만큼 돌아야 함. (큐에서는 N - 1번)
    for _ in range(N):
        min_node = 0
        for v in range(1, N):
            if visited[v]:
                continue
            if table[min_node] > table[v]:
                min_node = v
        visited[min_node] = True

        for v, e in graph[min_node]:
            new_cost = table[min_node] + e
            if table[v] > new_cost:
                table[v] = new_cost

    return table


graph = [
    [],
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    [],
]

result = dijkstra_simple(graph, 1)
print(result[1:])

# 0, 2, 3, 1, 2, 4



