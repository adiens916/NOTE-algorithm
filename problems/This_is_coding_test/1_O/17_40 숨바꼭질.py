import heapq


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# Dijkstra
INF = int(1e9)
distances = [INF] * (N + 1)

start, cost = 1, 0
distances[start] = cost
queue = [(cost, start)]
while queue:
    cost, start = heapq.heappop(queue)

    if cost > distances[start]:
        continue

    for v in graph[start]:
        new_cost = distances[start] + 1
        if distances[v] > new_cost:
            distances[v] = new_cost
            heapq.heappush(queue, (new_cost, v))

# 최단 거리가 제일 긴 곳 찾기
max_idx = 1
max_len = 0
count = 0
for i in range(2, N + 1):
    if distances[i] > max_len:
        max_idx = i
        max_len = distances[i]
        count = 1
    elif distances[i] == max_len:
        count += 1

print(max_idx, max_len, count)

"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""  # 4 2 3
