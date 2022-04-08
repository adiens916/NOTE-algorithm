"""
5 6
101010
111111
000001
111111
111111
"""


dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def bfs():
    front = rear = -1
    rear = (rear + 1) % SIZE
    queue[rear] = (0, 0, 1)
    arr[0][0] = 0

    while front != rear:
        front = (front + 1) % SIZE
        row, col, length = queue[front]

        for i in range(4):
            y = row + dy[i]
            x = col + dx[i]

            if not (0 <= x < M and 0 <= y < N):
                continue
            if not arr[y][x]:
                continue
            if y == N - 1 and x == M - 1:
                return length + 1
            # 방문
            arr[y][x] = 0
            rear = (rear + 1) % SIZE
            queue[rear] = (y, x, length + 1)



N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

SIZE = N * M
queue = [0] * SIZE

print(bfs())
