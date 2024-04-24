from collections import deque

WALL = 1
BLANK = 0
H = 1
V = 0

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

visited_h = [[False] * N for _ in range(N)]
visited_v = [[False] * N for _ in range(N)]


def solution(board):
    answer = 0
    return answer


def bfs(N: int):
    start = ((0, 0), (0, 1), H)
    queue = deque([start])

    visited_h[0][0] = True
    visited_h[0][1] = True

    while queue:
        tail, head, d = queue.popleft()

        for i in range(4):
            n_tail, n_head = move(tail, head, i)

            if not is_in_board(tail, head, N):
                continue

            if is_visited(tail, head, d):
                continue

            visit(tail, head, d)


def move(tail: tuple, head: tuple, i: int) -> tuple:
    n_tail_y = tail[0] + dy[i]
    n_tail_x = tail[1] + dx[i]
    n_head_y = head[0] + dy[i]
    n_head_x = head[1] + dx[i]
    return (n_tail_y, n_tail_x), (n_head_y, n_head_x)


def is_in_board(tail: tuple, head: tuple, N: int) -> bool:
    a = 0 <= tail[0] < N and 0 <= tail[1] < N
    b = 0 <= head[0] < N and 0 <= head[1] < N
    return a and b


def is_visited(tail: tuple, head: tuple, d: int) -> bool:
    if d == H:
        v1 = visited_h[tail[0]][tail[1]]
        v2 = visited_h[head[0]][head[1]]
    else:
        v1 = visited_v[tail[0]][tail[1]]
        v2 = visited_v[head[0]][head[1]]
    return v1 and v2


def visit(tail, head, d) -> None:
    if d == H:
        visited_h[tail[0]][tail[1]] = True
        visited_h[head[0]][head[1]] = True
    else:
        visited_v[tail[0]][tail[1]] = True
        visited_v[head[0]][head[1]] = True
