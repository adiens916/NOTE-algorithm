from collections import deque


N, M = map(int, input().split())
ice_map = [list(input()) for _ in range(N)]

move_types = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def check_visited(y: int, x: int, graph: list[list[str]]) -> None:
    # BFS
    start = (y, x)
    queue = deque([start])

    while any(queue):
        y, x = queue.popleft()

        if graph[y][x] == "1":
            continue
        graph[y][x] = "1"

        for move in move_types:
            dy = move[0]
            dx = move[1]
            if 0 <= y + dy < N and 0 <= x + dx < M:
                queue.append((y + dy, x + dx))


count = 0

for y in range(N):
    for x in range(M):
        if ice_map[y][x] == "0":
            count += 1
            check_visited(y, x, ice_map)

print(count)

"""
4 5
00110
00011
11111
00000
"""
"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""
