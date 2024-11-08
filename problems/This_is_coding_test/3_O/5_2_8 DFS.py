result = []
visited = [False] * 10


def dfs(graph: list[list[int]], start: int) -> None:
    for v in graph[start]:
        if visited[v]:
            continue

        visited[v] = True
        result.append(v)
        dfs(graph, v)


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start = 1
result.append(start)
visited[start] = True

dfs(graph, start)
print(result)

"""
8 9
1 2
1 3
1 8
2 7
3 4
3 5
4 5
6 7
7 8
"""
