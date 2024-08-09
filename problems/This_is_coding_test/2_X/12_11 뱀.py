from collections import deque

APPLE = 2

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]
for _ in range(K):
    Y, X = map(int, input().split())
    # XXX: 행열 시작이 0인지 1인지 확인
    board[Y - 1][X - 1] = APPLE

L = int(input())

dirs = []
for _ in range(L):
    X, C = input().split()
    dirs.append((int(X), C))


def dummy(board, dirs) -> int:
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]

    t = 0
    snake = [(0, 0)]
    snake = deque(snake)
    board[0][0] = 1
    snake_d = 0
    dir_i = 0

    while True:
        t += 1

        y = snake[-1][0] + dy[snake_d]
        x = snake[-1][1] + dx[snake_d]

        if not (0 <= y < N and 0 <= x < N):
            break

        if board[y][x] == 1:
            break

        if board[y][x] != APPLE:
            tail = snake.popleft()
            board[tail[0]][tail[1]] = 0
        snake.append((y, x))
        board[y][x] = 1

        # XXX: 계속 증가하는 거 막아야 함.
        if dir_i == len(dirs) or dirs[dir_i][0] > t:
            continue
        else:
            if dirs[dir_i][1] == 'L':
                snake_d = (snake_d + 1) % 4
            else:
                snake_d = (snake_d - 1) % 4
            dir_i += 1

    return t


print(dummy(board, dirs))
