from collections import deque


def topology_sort(graph: list[list[int]]) -> list[int]:
    N = len(graph)
    in_degrees = [0] * N
    for v in range(N):
        for next_ in graph[v]:
            in_degrees[next_] += 1
    visited = [False] * N

    queue = deque([])
    for v in range(1, N):
        if in_degrees[v] == 0:
            queue.append(v)
            visited[v] = True

    result = []
    while queue:
        v = queue.popleft()
        result.append(v)

        for next_ in graph[v]:
            # XXX: visited 대신에 in_degree로 하는 게 깔끔함
            # in_degree가 0이면 넘어가는 식
            if visited[next_]:
                continue

            in_degrees[next_] -= 1
            if in_degrees[next_] == 0:
                queue.append(next_)
                visited[next_] = True

    return result


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)

result = topology_sort(graph)
print(result)

"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
