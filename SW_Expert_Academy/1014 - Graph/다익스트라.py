INF = 987654321
V = int(input())
adj = [[]]
visited = [False] * V
D = [INF] * V

def dijkstra(s):
    D[s] = 0
    for i in range(V):
        # 최솟값 찾기
        min_value = INF
        for j in range(V):
            if not visited[j] and D[j] < min_value:
                min_value = D[j]
                u = j
        
        # 방문체크
        visited[u] = True

        # 인접 정점 업데이트
        for v in range(V):
            if adj[u][v] and not visited[v]:
                D[v] = min(D[v], D[u] + adj[u][v])  # 출발점 + 경로
