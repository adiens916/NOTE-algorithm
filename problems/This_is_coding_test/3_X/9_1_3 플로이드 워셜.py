def floyd_warshall(graph: list[list[int]]) -> None:
    N = len(graph) - 1

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                # XXX: 시작점과 도착점이 같은 경우 체크는 굳이 필요 없음.
                # 0이면 min 값도 0이 되기 때문.
                # if graph[a][b] == 0:
                #     continue

                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# XXX: 못 가는 경우 INF로 세팅 중요.
INF = int(1e9)
graph = [
    [0, 0, 0, 0, 0],
    [0, 0, 4, INF, 6],
    [0, 3, 0, 7, INF],
    [0, 5, INF, 0, 4],
    [0, INF, INF, 2, 0],
]

floyd_warshall(graph)
for line in graph:
    print(line)

""" #
[0, 4, 8, 6]
[3, 0, 7, 9]
[5, 9, 0, 4]
[7, 11, 2, 0]
"""