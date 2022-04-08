"""
p. 149 음료수 얼려 먹기

범위는 1000 * 1000
=> 그런데 큐에 들어가 살펴보는 것도 1M
=> 따라서 시간 복잡도는 O(N)

입력
4 5
00110
00011
11111
00000
"""


dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def bfs(row, col):
    front = rear = -1
    rear = (rear + 1) % SIZE
    queue[rear] = (row, col)
    visited[row][col] = True

    while front != rear:
        front = (front + 1) % SIZE
        row, col = queue[front]

        for i in range(4):
            y = row + dy[i]
            x = col + dx[i]

            if not (0 <= x and x < M and 0 <= y and y < N):
                continue
            if visited[y][x]:
                continue
            if arr[y][x] == 1:
                continue
            visited[y][x] = True
            rear = (rear + 1) % SIZE
            queue[rear] = (y, x)


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

SIZE = N * M
queue = [0] * SIZE
visited = [[False] * M for _ in range(N)]
ice_sector = 0

for row in range(N):
    for col in range(M):
        if arr[row][col] == 0 and \
            not visited[row][col]:
            bfs(row, col)
            ice_sector += 1

print(ice_sector)
