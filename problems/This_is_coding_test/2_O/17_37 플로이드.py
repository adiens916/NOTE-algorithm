N = int(input())
M = int(input())

INF = int(1e9)
graph = [[INF] * N for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A-1][B-1] = min(graph[A-1][B-1], C)

# Floyd-Warshall
for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for y in range(N):
    for x in range(N):
        if graph[y][x] == INF:
            graph[y][x] = 0
        if y == x:
            graph[y][x] = 0

for y in range(N):
    print(*graph[y], sep=' ')
