from collections import deque


def bfs(start: int, graph: list[list[int]]) -> None:
    visited = [False] * (len(graph) + 1)
    queue = deque([start])
    visited[start] = True

    while any(queue):
        start = queue.popleft()
        print(start, end=" ")

        for v in graph[start]:
            if visited[v]:
                continue
            queue.append(v)
            visited[v] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

bfs(1, graph)
