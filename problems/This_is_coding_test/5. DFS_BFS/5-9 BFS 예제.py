"""
5-9. BFS 예제
그래프를 방문하는 순서대로 출력
"""

from typing import List


def bfs(graph: List[List[int]], start: int, visited: List[bool]):
    SIZE = len(graph)
    queue = [0] * SIZE
    front = rear = -1

    rear = (rear + 1) % SIZE
    queue[rear] = start
    visited[start] = True

    # FIXME: 큐 종료 조건
    while front != rear:
        front = (front + 1) % SIZE
        v = queue[front]
        print(v, end=' ')

        for w in graph[v]:
            if not visited[w]:
                rear = (rear + 1) % SIZE
                queue[rear] = w
                visited[w] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * len(graph)

bfs(graph, 1, visited)
