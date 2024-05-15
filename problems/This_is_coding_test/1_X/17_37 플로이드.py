MAX = int(1e9)

n = int(input())
m = int(input())

graph = [[MAX] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 시작 도시랑 도착 도시가 같은 경우는 없음
for i in range(1, n + 1):
    graph[n][n] = 0

# Floyd-Warshall Alg.
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for r in range(1, n + 1):
    for c in range(1, n + 1):
        # 갈 수 없으면 0으로 출력
        if graph[r][c] == MAX:
            graph[r][c] = 0
        print(graph[r][c], end=' ')
    print()

"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""
"""  #
0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0
"""
