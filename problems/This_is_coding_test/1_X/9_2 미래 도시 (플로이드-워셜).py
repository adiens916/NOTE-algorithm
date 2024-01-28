N, M = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]  # XXX: 만들 때부터 초기화하면 더 빠름
for V in range(1, N + 1):  # XXX: 인접 행렬에서 자기 자신은 0으로 초기화
    graph[V][V] = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

X, K = map(int, input().split())


# 모든 지점에서 다른 지점으로의 최단 경로 찾기 (by 플로이드-워셜 알고리즘)
for mid in range(1, N + 1):
    for A in range(1, N + 1):
        for B in range(1, N + 1):
            graph[A][B] = min(graph[A][B], graph[A][mid] + graph[mid][B])

min_distance = graph[1][K] + graph[K][X]
if min_distance >= INF:
    min_distance = -1
print(min_distance)


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
"""  # -1
