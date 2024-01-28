import heapq


N, M = map(int, input().split())

# XXX: 이중 리스트 선언 시 그냥 [[]] * (N + 1)하면 안됨
# 저 방식은 (id가) 같은 객체를 그냥 똑같이 복사하는 것 (얕은 복사)
# 그래서 append하면 해당 (id가) 같은 객체들 전부에 추가됨
# <=> 리스트 컴프리헨션은 매번 새로운 []을 생성하는 방식임
graph: list[list[int]] = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    # XXX: 무방향 그래프에서는 반대편도 똑같이 추가해야 함
    graph[B].append(A)
X, K = map(int, input().split())


INF = int(1e9)


# XXX: 다익스트라로도 풀 수는 있지만 비효율적.
# 이미 계산했던 거리를 또 다시 계산해야 함.
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
"""  # 3

"""
4 2
1 3
2 4
3 4
"""
