from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)


def bfs(graph, K, X):
    result = []
    queue = deque([(X, 0)])

    visited = [False] * (N + 1)
    visited[X] = True

    while queue:
        node, dist = queue.popleft()

        for v in graph[node]:
            if visited[v]:
                continue
            visited[v] = True

            if dist + 1 == K:
                result.append(v)
            else:
                queue.append((v, dist + 1))

    return result


result = bfs(graph, K, X)
if len(result) == 0:
    print(-1)
else:
    # XXX: 오름차순 정렬 까먹음. 조건을 적어놓자.
    result.sort()
    print(*result, sep='\n')
