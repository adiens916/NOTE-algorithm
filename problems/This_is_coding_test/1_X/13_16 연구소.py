from itertools import combinations
from collections import deque

BLANK = 0
WALL = 1
VIRUS = 2


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# XXX: 임시 지도를 하나 더 만들고, 거기서 작업하면 원본 보존 가능.
temp = [[0] * M for _ in range(N)]


def main():
    blanks = []
    for row in range(N):
        for col in range(M):
            if arr[row][col] == BLANK:
                blanks.append((row, col))

    # XXX: 빈 곳 3개를 조합으로 고르기
    wall_candidates = combinations(blanks, 3)

    max_safe_zone = 0
    for wall_candidate in wall_candidates:
        for wall_r, wall_c in wall_candidate:
            arr[wall_r][wall_c] = WALL

        spread_virus(arr, temp)
        cur_safe_zone = count_safe_zone(temp)
        max_safe_zone = max(max_safe_zone, cur_safe_zone)

        for wall_r, wall_c in wall_candidate:
            arr[wall_r][wall_c] = BLANK

    print(max_safe_zone)


def spread_virus(arr, temp) -> None:
    for y in range(N):
        for x in range(M):
            temp[y][x] = arr[y][x]

    for y in range(N):
        for x in range(M):
            if temp[y][x] == VIRUS:
                bfs(temp, y, x)


def bfs(temp, row, col):
    dy = (0, 0, 1, -1)
    dx = (1, -1, 0, 0)

    queue = deque([(row, col)])

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            y = row + dy[i]
            x = col + dx[i]

            if not (0 <= y < N and 0 <= x < M):
                continue

            if temp[y][x] == BLANK:
                temp[y][x] = VIRUS
                queue.append((y, x))


def count_safe_zone(temp) -> int:
    count = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == BLANK:
                count += 1
    return count


main()

"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""  # 27
"""
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
"""  # 3
