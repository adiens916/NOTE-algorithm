def dijkstra_simple(
    graph: list[list[tuple[int, int]]], N: int, start: int
) -> list[int]:
    INF = int(1e9)
    min_lengths = [INF] * (N + 1)
    visited = [False] * (N + 1)

    min_lengths[start] = 0
    visited[start] = True
    # XXX
    for v, e in graph[start]:
        min_lengths[v] = e

    def get_node_of_min_length() -> int:
        # XXX
        min_value = INF
        min_index = 0

        for i in range(1, N + 1):
            if not visited[i] and min_lengths[i] < min_value:
                min_value = min_lengths[i]
                min_index = i

        return min_index

    # XXX
    for _ in range(N - 1):
        now = get_node_of_min_length()
        visited[now] = True

        for v, e in graph[now]:
            cost = min_lengths[now] + e
            if cost < min_lengths[v]:
                min_lengths[v] = cost

    return min_lengths


graph = [
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
]

min_lengths = dijkstra_simple(graph, 6, 0)
print(min_lengths)
