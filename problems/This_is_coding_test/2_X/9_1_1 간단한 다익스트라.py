# 간단한 다익스트라에선 큐를 이용하지 않음.
# 가장 작은 인덱스만 뽑아와서 비교함.

INF = int(1e9)


def get_shortest_path(queue: list[tuple[int, int]]) -> tuple[int, int]:
    min_index = 0
    for i in range(1, len(queue)):
        if queue[i][0] < queue[min_index][0]:
            min_index = i
    item = queue.pop(min_index)
    return item


def dijkstra_simple(graph: list[list[int]], start: int) -> list[int]:
    N = len(graph)
    table = [INF] * N
    table[start] = 0

    queue = [(0, start)]
    while queue:
        length, start = get_shortest_path(queue)
        if table[start] < length:
            continue

        for v, e in graph[start]:
            cur_cost = table[start] + e
            if cur_cost < table[v]:
                table[v] = cur_cost
                queue.append((cur_cost, v))

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
