import heapq

graph = [
    [],
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    [],
]
N = len(graph) - 1

INF = int(1e9)
min_lengths = [INF] * (N + 1)


def dijkstra_with_priority_queue(start: int) -> list[int]:
    min_lengths[start] = 0

    priority_queue = [(0, start)]

    # 달라지는 부분
    while any(priority_queue):
        edge, start = heapq.heappop(priority_queue)
        # XXX: 방문 여부 대신에, 거리가 더 짧은지로 비교 가능
        # 어차피 방문한(처리한) 경우, 거리는 항상 최소이기 때문.
        if min_lengths[start] < edge:
            continue

        for dest, edge in graph[start]:
            cost = min_lengths[start] + edge
            if cost < min_lengths[dest]:
                min_lengths[dest] = cost
                # 달라지는 부분
                heapq.heappush(priority_queue, (edge, dest))

    return min_lengths


result = dijkstra_with_priority_queue(1)
print(result[1:])
