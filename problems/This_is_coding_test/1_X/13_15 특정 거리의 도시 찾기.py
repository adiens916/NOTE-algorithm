from collections import deque
import sys


input = sys.stdin.readline  # XXX: 이걸 쓰면 200ms 더 빨라짐

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)


def bfs(graph, start, target_len):
    target_nodes = []

    queue = deque([(start, 0)])
    visited = [False] * (N + 1)
    visited[start] = True

    while queue:
        start, length = queue.popleft()

        for next in graph[start]:
            if visited[next]:
                continue

            # 목표 도시인 경우, 더 이상 갈 필요없음.
            if length + 1 == target_len:
                target_nodes.append(next)
            # 아직 목표까지 도달하지 못한 경우, 큐에 넣어서 더 가기.
            else:
                queue.append((next, length + 1))

            # XXX: 다음이 목표 도시든 아니든, 무조건 방문한 건 맞음.
            visited[next] = True

    return target_nodes


target_nodes = bfs(graph, X, K)
if len(target_nodes) == 0:
    print(-1)
else:
    target_nodes.sort()
    print(*target_nodes, sep="\n")

"""
4 4 2 1
1 2
1 3
2 3
2 4
"""  # 4
"""
4 3 2 1
1 2
1 3
1 4
"""  # -1
"""
4 4 1 1
1 2
1 3
2 3
2 4
"""  # 2 3
