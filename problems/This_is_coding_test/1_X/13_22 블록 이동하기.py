from collections import deque

WALL = 1
BLANK = 0

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)


def solution(board):
    surround(board)
    answer = bfs(board)
    return answer


def surround(board: list) -> None:
    N = len(board)
    board.insert(0, [WALL] * N)
    board.append([WALL] * N)
    for line in board:
        line.insert(0, WALL)
        line.append(WALL)


def bfs(board: list) -> int:
    n = len(board) - 2

    start = ((1, 1), (1, 2))
    count = 0
    queue = deque([(start, count)])

    visited = set()
    visited.add(start)

    while queue:
        pos_list, count = queue.popleft()

        # 회전하는 경우 체크
        for pos_list_r in rotate(pos_list, board):
            if pos_list_r in visited:
                continue

            if not is_in_goal(pos_list_r, n):
                visited.add(pos_list_r)
                queue.append((pos_list_r, count + 1))
            else:
                return count + 1

        # 이동하는 경우 체크
        for pos_list_m in move(pos_list, board):
            if pos_list_m in visited:
                continue

            if not is_in_goal(pos_list_m, n):
                visited.add(pos_list_m)
                queue.append((pos_list_m, count + 1))
            else:
                return count + 1


def rotate(pos_list: tuple, board: list) -> list:
    result = []

    pos1, pos2 = pos_list
    pos1_y, pos1_x = pos1
    pos2_y, pos2_x = pos2

    # 가로인 경우
    if pos1_y == pos2_y:
        # 위에 벽 없으면 회전
        if board[pos1_y - 1][pos1_x] == BLANK and board[pos2_y - 1][pos2_x] == BLANK:
            a = ((pos1_y - 1, pos1_x), (pos1_y, pos1_x))
            b = ((pos2_y - 1, pos2_x), (pos2_y, pos2_x))
            result.append(a)
            result.append(b)

        # 아래에 벽 없으면 회전
        if board[pos1_y + 1][pos1_x] == BLANK and board[pos2_y + 1][pos2_x] == BLANK:
            a = ((pos1_y, pos1_x), (pos1_y + 1, pos1_x))
            b = ((pos2_y, pos2_x), (pos2_y + 1, pos2_x))
            result.append(a)
            result.append(b)

    # 세로인 경우
    else:
        # 오른쪽 벽 없으면 회전
        if board[pos1_y][pos1_x + 1] == BLANK and board[pos2_y][pos2_x + 1] == BLANK:
            a = ((pos1_y, pos1_x), (pos1_y, pos1_x + 1))
            b = ((pos2_y, pos2_x), (pos2_y, pos2_x + 1))
            result.append(a)
            result.append(b)

        # 왼쪽에 벽 없으면 회전
        if board[pos1_y][pos1_x - 1] == BLANK and board[pos2_y][pos2_x - 1] == BLANK:
            a = ((pos1_y, pos1_x - 1), (pos1_y, pos1_x))
            b = ((pos2_y, pos2_x - 1), (pos2_y, pos2_x))
            result.append(a)
            result.append(b)

    return result


def move(pos_list: tuple, board: list) -> list:
    result = []

    pos1, pos2 = sorted(pos_list)
    pos1_y, pos1_x = pos1
    pos2_y, pos2_x = pos2

    for i in range(4):
        n_pos1_y = pos1_y + dy[i]
        n_pos1_x = pos1_x + dx[i]
        n_pos2_y = pos2_y + dy[i]
        n_pos2_x = pos2_x + dx[i]

        if board[n_pos1_y][n_pos1_x] == BLANK and board[n_pos2_y][n_pos2_x] == BLANK:
            pos_list = ((n_pos1_y, n_pos1_x), (n_pos2_y, n_pos2_x))
            result.append(pos_list)

    return result


def is_in_goal(pos_list: set, n: int) -> bool:
    pos1, pos2 = pos_list
    pos1_y, pos1_x = pos1
    pos2_y, pos2_x = pos2

    a = pos1_y == n and pos1_x == n
    b = pos2_y == n and pos2_x == n
    return a or b


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
# 7
