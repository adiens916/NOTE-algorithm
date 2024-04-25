from collections import deque

WALL = 1
BLANK = 0

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)


def solution(board):
    answer = bfs(board)
    return answer


def bfs(board: list) -> int:
    N = len(board)

    start = {(0, 0), (0, 1)}
    count = 0
    queue = deque([(start, count)])

    visited = set()
    visited.add(start)

    while queue:
        pos_set, count = queue.popleft()
        pos1, pos2 = list(pos_set)
        pos1_y, pos1_x = pos1
        pos2_y, pos2_x = pos2

        for pos_set_r in rotate(pos_set, board):
            if pos_set_r in visited:
                continue

            for pos_set_m in move(pos_set_r, board):
                if pos_set_m in visited:
                    continue

                if not is_in_goal(pos_set_m, N):
                    visited.add(pos_set_m)
                    queue.append((pos_set_m, count + 1))
                else:
                    return count


def rotate(pos_set: set, board: list) -> list:



def move(tail: tuple, head: tuple, i: int) -> tuple:
    for i in range(4):
        n_tail, n_head = move(tail, head, i)
    n_tail_y = tail[0] + dy[i]
    n_tail_x = tail[1] + dx[i]
    n_head_y = head[0] + dy[i]
    n_head_x = head[1] + dx[i]
    return (n_tail_y, n_tail_x), (n_head_y, n_head_x)


def is_in_goal(pos_set: set, n: int) -> bool:
    pos1, pos2 = list(pos_set)
    pos1_y, pos1_x = pos1
    pos2_y, pos2_x = pos2

    a = pos1_y == n - 1 and pos1_x == n - 1
    b = pos2_y == n - 1 and pos2_x == n - 1
    return a or b
