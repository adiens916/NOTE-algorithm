from collections import deque


N, M = map(int, input().split())
labyrinth = [list(input()) for _ in range(N)]

move_types = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(y: int, x: int, graph: list[list[str]]) -> int:
    start = (y, x, 0)
    queue = deque([start])

    while any(queue):
        y, x, length = queue.popleft()

        if graph[y][x] == "0":
            continue
        graph[y][x] = "0"
        length += 1

        if y == N - 1 and x == M - 1:
            return length

        for dy, dx in move_types:
            if 0 <= y + dy < N and 0 <= x + dx < M:
                queue.append((y + dy, x + dx, length))


length = bfs(0, 0, labyrinth)
print(length)

"""
5 6
101010
111111
000001
111111
111111
"""
