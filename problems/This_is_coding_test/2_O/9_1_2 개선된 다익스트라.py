import heapq


def dijkstra(graph: list[list[int]], start: int) -> list[int]:
    N = len(graph)
    INF = int(1e9)
    table = [INF] * N
    table[start] = 0

    queue = [(0, start)]
    while queue:
        cost, start = heapq.heappop(queue)

        if table[start] < cost:
            continue

        for v, e in graph[start]:
            new_cost = table[start] + e
            if table[v] > new_cost:
                table[v] = new_cost
                heapq.heappush(queue, (new_cost, v))

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

result = dijkstra(graph, 1)
print(result[1:])
