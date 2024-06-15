from collections import deque


def topology_sort(graph: list[list[int]]) -> list[int]:
    N = len(graph)
    in_degrees = [0] * N
    for v in range(N):
        for next_ in graph[v]:
            in_degrees[next_] += 1

    queue = deque([])
    for v in range(1, N):
        if in_degrees[v] == 0:
            queue.append(v)

    result = []
    while queue:
        v = queue.popleft()
        result.append(v)

        for next_ in graph[v]:
            # XXX: visited 대신에 in_degree로 하는 게 더 깔끔함
            # 어차피 비교 연산이나 빼기 연산이나 비슷함
            in_degrees[next_] -= 1

            # in_degree가 0이 됐을 때'만' 넣으면 됨.
            if in_degrees[next_] == 0:
                queue.append(next_)

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
"""  # 1 2 5 3 6 4 7
