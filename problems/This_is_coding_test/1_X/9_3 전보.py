import heapq

N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))


INF = int(1e9)


def dijkstra(start: int) -> list[int]:
    min_lengths = [INF] * (N + 1)
    min_lengths[start] = 0
    visited = [False] * (N + 1)

    queue = [(0, start)]
    while any(queue):
        edge, start = heapq.heappop(queue)

        # XXX: 이 부분은 visited 안 써도 됨
        # 결국 방문했던 거면 지금보다 거리가 더 짧은 것이었기에,
        # if min_lengths[start] < edge인지 보면 됨.
        if visited[start]:
            continue
        visited[start] = True

        for dest, edge in graph[start]:
            cost = min_lengths[start] + edge
            if cost < min_lengths[dest]:
                min_lengths[dest] = cost
                heapq.heappush(queue, (cost, dest))

    return min_lengths


min_lengths = dijkstra(C)

reachable_count = 0
max_length = 0

for length in min_lengths[1:]:
    if length == INF or length == 0:
        continue

    reachable_count += 1
    max_length = max(max_length, length)

print(reachable_count, max_length)


"""
3 2 1
1 2 4
1 3 2
"""  # 2 4
