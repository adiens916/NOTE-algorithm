# https://www.acmicpc.net/problem/17086


def get_starts(arr):
    starts = []
    for row in range(N):
        for col in range(M):
            if arr[row][col] == 1:
                starts.append((row, col))
    return starts


def bfs(arr):
    # 상하좌우, 좌상, 우상, 좌하, 우하
    dy = (-1, 1, 0, 0, -1, -1, 1, 1)
    dx = (0, 0, -1, 1, -1, 1, -1, 1)

    max_len = 0

    SIZE = N * M
    queue = [0] * SIZE
    front = rear = -1

    starts = get_starts(arr)
    for row, col in starts:
        rear = (rear + 1) % SIZE
        queue[rear] = (row, col)
    
    while front != rear:
        front = (front + 1) % SIZE
        row, col = queue[front]

        for i in range(8):
            y = row + dy[i]
            x = col + dx[i]

            if not (0 <= x < M and 0 <= y < N):
                continue
            if arr[y][x]:
                continue
            arr[y][x] = arr[row][col] + 1
            max_len = arr[y][x]

            rear = (rear + 1) % SIZE
            queue[rear] = (y, x)
        
    return max_len


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_len = bfs(arr)
print(max_len - 1)


"""
7 4
0 0 0 1
0 1 0 0
0 0 0 0
0 0 0 1
0 0 0 0
0 1 0 0
0 0 0 1
"""
