"""
N*N
아기 상어 크기 2에서 시작
1초마다 한 칸씩
같으면 지나가고, 작으면 먹음. 크면 못 지나감
가까운 물고기 - 위 - 왼쪽 순으로 먹음.
  => 매번 거리 계산 후, 정렬

현재 크기와 같은 수만큼 먹으면 크기 증가
몇 초동안 먹는지
"""
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

shark_y, shark_x = 0, 0
for row in range(N):
    for col in range(N):
        if arr[row][col] == 9:
            shark_y, shark_x = row, col
            arr[row][col] = 0

dy = (0, -1, 0, 1)
dx = (1, 0, -1, 0)
shark_size = 2


def bfs(row, col):
    result = []
    visited = [[False] * N for _ in range(N)]
    visited[row][col] = True

    queue = deque([(row, col, 0)])
    while queue:
        row, col, t = queue.popleft()

        for i in range(4):
            y = row + dy[i]
            x = col + dx[i]

            if not (0 <= y < N and 0 <= x < N):
                continue
            if visited[y][x]:
                continue

            visited[y][x] = True
            # 작거나 같으면 지나감.
            if arr[y][x] <= shark_size:
                queue.append((y, x, t + 1))
                # XXX: 상어 사이즈보다 작아야 먹음.
                if 0 < arr[y][x] < shark_size:
                    result.append((t + 1, y, x))

    return result


t = 0
eaten_num = 0
while True:
    # 가능한 리스트 추출
    fish_list = bfs(shark_y, shark_x)
    if len(fish_list) == 0:
        print(t)
        break

    # 거리 - Y축 - X축 순으로 정렬
    fish_list.sort()
    # 최선의 후보 찾음
    t_add, fish_y, fish_x = fish_list[0]

    # 가서 대체함
    t += t_add
    shark_y, shark_x = fish_y, fish_x
    arr[fish_y][fish_x] = 0

    # 먹고 크기 늘리는 부분
    eaten_num += 1
    if eaten_num == shark_size:
        shark_size += 1
        eaten_num = 0
