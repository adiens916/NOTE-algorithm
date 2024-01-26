import heapq


N, M = map(int, input().split())

graph: list[list[int]] = [[]] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
X, K = map(int, input().split())


INF = int(1e9)


def dijkstra(start: int) -> list[int]:
    min_lengths = [INF] * (N + 1)
    min_lengths[start] = 0
    queue = [(0, start)]
    visited = [False] * (N + 1)

    while any(queue):
        edge, start = heapq.heappop(queue)
        if visited[start]:
            continue
        visited[start] = True

        for dest in graph[start]:
            cost = min_lengths[start] + 1
            if cost < min_lengths[dest]:
                min_lengths[dest] = cost
                heapq.heappush(queue, (cost, dest))

    return min_lengths


distances_from_start = dijkstra(1)
distance_to_cafe = distances_from_start[K]

distances_from_cafe = dijkstra(K)
distance_to_sales = distances_from_cafe[X]

shortest_length = distance_to_cafe + distance_to_sales
if shortest_length < INF:
    print(shortest_length)
else:
    print(-1)


"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""
