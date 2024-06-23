N, M = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())


# Floyd-Warshall
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = graph[1][K] + graph[K][X]
if answer >= INF:
    print(-1)
else:
    print(answer)

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
"""
4 2
1 3
2 4 
3 4
"""