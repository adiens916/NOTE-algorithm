V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (V + 1)


def dfs(start: int):
    # 1. 방문 처리
    visited[start] = True
    print(start)

    # 2. 인접 노드 확인
    for v in graph[start]:
        # 3. 방문하지 않았으면 DFS
        if visited[v]:
            continue
        dfs(v)


dfs(1)
