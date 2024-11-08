from collections import deque


def bfs(graph: list[list[int]], start: int) -> list[int]:
    result = [start]
    visited = [False] * len(graph)
    visited[start] = True

    queue = deque([start])
    while queue:
        start = queue.popleft()

        for v in graph[start]:
            if visited[v]:
                continue

            visited[v] = True
            result.append(v)
            queue.append(v)

    return result


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = bfs(graph, 1)
print(result)
