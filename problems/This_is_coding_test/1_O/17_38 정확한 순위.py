N, M = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (N + 1) for _  in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1

# 다른 학생들까지 가는 경로가 있는지 확인 (플로이드-워셜 알고리즘)
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 성적 비교
knowable = 0
for i in range(1, N + 1):
    lower_score_count = 0
    for j in range(1, N + 1):
        if 0 < graph[j][i] < INF:
            lower_score_count += 1

    higher_score_count = 0
    for j in range(1, N + 1):
        if 0 < graph[i][j] < INF:
            higher_score_count += 1

    if lower_score_count + higher_score_count + 1 == N:
        knowable += 1

print(knowable)

"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""  # 1
