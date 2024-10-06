"""
번호가 낮은 바이러스부터 증식
이미 있으면 못 들어감
바이러스가 없는 곳은 0
1, 1부터 시작
"""

from collections import deque

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

viruses = []
for r in range(N):
    for c in range(N):
        if arr[r][c] != 0:
            # XXX: 시간도 넣기
            viruses.append((arr[r][c], r, c, 0))
viruses.sort()


def bfs():
    dy = (-1, 0, 1, 0)
    dx = (0, -1, 0, 1)

    queue = deque(viruses)

    while queue:
        virus, r, c, t = queue.popleft()

        # XXX: S초가 되었을 때 종료
        if t == S:
            break

        for i in range(4):
            y = r + dy[i]
            x = c + dx[i]

            if not (0 <= y < N and 0 <= x < N):
                continue

            if arr[y][x] == 0:
                arr[y][x] = virus
                # XXX: 시간 1 증가시켜서 넣기
                queue.append((virus, y, x, t + 1))


bfs()
print(arr[X - 1][Y - 1])
