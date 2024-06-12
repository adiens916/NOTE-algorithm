import heapq


N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append([Y, Z])

INF = int(1e9)


def dijkstra(graph: list[list[int]], start: int) -> list[int]:
    table = [INF] * len(graph)
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


table = dijkstra(graph, C)
count = 0
max_time = 0
for i in range(1, N + 1):
    if table[i] != INF:
        count += 1
        max_time = max(max_time, table[i])

print(count - 1, max_time)

"""
3 2 1
1 2 4
1 3 2
"""  # 2 4
