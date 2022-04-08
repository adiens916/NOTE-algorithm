import heapq


V, E = map(int, input().split())
W = [[0] * (V + 1)]
for i in range(E):
    s, e, w = map(int, input().split())
    W[s].append((e, w))


def dijkstra(start):
    INF = 1e9
    costs = [INF] * (V + 1)
    costs[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, v = heapq.heappop(heap)

        if cost > costs[v]:
            continue
        
        for e, w in W[s]:
            if costs[e] > costs[s] + w:
                costs[e] = costs[s] + w
                heapq.heappush(heap, (costs[e], e))

dijkstra(1)