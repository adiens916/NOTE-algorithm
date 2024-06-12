def floyd_warshall(graph: list[list[int]]) -> list[list[int]]:
    N = len(graph)
    
    for k in range(N):
        for a in range(N):
            for b in range(N):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    return graph


# XXX: 못 가는 건 0이 아니라 무한대로 따로 표시해야 함
# 0으로 표기하면, 모든 경로가 다 0이 되어버림
# 왜냐하면 두 지점 간 거리는 원래대로면 0보다 큰 값이 나오는데,
# 비교 과정에서 0보다 크니까 전부 0으로 바뀜.
INF = int(1e9)
graph = [
    [0, 4, INF, 6],
    [3, 0, 7, INF],
    [5, INF, 0, 4],
    [INF, INF, 2, 0],
]

result = floyd_warshall(graph)
for line in result:
    print(line)

""" #
[0, 4, 8, 6]
[3, 0, 7, 9]
[5, 9, 0, 4]
[7, 11, 2, 0]
"""
