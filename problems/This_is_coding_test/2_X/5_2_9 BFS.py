from collections import deque


V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (V + 1)
# 0. 시작 지점 방문 처리
visited[1] = True


def bfs(start: int):
    queue = deque([start])
    while queue:
        start = queue.popleft()
        # 1. 할 일 하기
        print(start)

        for v in graph[start]:
            # 2. 주변 탐색
            if visited[v]:
                continue
            # 3. 방문하지 않았으면 (즉, 처음 보는 거면) 체크
            visited[v] = True
            queue.append(v)


bfs(1)
