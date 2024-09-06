"""
빈 칸, 벽 있음.
새로 세울 수 있는 벽 개수 3개 꼭 설치
안전 영역 크기 최댓값 구하기
"""
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

safes = []
viruses = []
for r in range(N):
    for c in range(M):
        if arr[r][c] == 0:
            safes.append((r, c))
        elif arr[r][c] == 2:
            viruses.append((r, c))

max_zone = 0

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def bfs() -> None:
    global max_zone

    new_arr = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            new_arr[r][c] = arr[r][c]

    queue = deque(viruses)
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            y = r + dy[i]
            x = c + dx[i]

            if not (0 <= y < N and 0 <= x < M):
                continue

            if new_arr[y][x] == 0:
                new_arr[y][x] = 2
                queue.append((y, x))

    cur_zone = 0
    for r in range(N):
        for c in range(M):
            if new_arr[r][c] == 0:
                cur_zone += 1
    max_zone = max(max_zone, cur_zone)


checked = [False] * len(safes)


def combination(k, now) -> None:
    if now == k:
        bfs()
    else:
        for i in range(len(checked)):
            if checked[i]:
                continue
            else:
                checked[i] = True
                r, c = safes[i]
                arr[r][c] = 1

                combination(k, now + 1)

                arr[r][c] = 0
                checked[i] = False


combination(3, 0)
print(max_zone)
