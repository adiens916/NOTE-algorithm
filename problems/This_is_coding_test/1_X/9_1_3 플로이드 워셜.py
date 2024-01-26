def floyd_warshall(graph: list[list[int]]) -> None:
    N = len(graph)

    for k in range(N):
        for a in range(N):
            for b in range(N):
                # if graph[a][b] > graph[a][k] + graph[k][b]:
                #     graph[a][b] = graph[a][k] + graph[k][b]
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


INF = int(1e9)
graph = [
    [0, 4, INF, 6],
    [3, 0, 7, INF],
    [5, INF, 0, 4],
    [INF, INF, 2, 0],
]

floyd_warshall(graph)
for line in graph:
    print(line)
