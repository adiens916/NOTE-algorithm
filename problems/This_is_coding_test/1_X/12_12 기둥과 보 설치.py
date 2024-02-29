COL = 0
ROW = 1
COLROW = 2

DEL = 0
BIL = 1


def is_col(board, y, x) -> bool:
    return board[y][x] == COL or board[y][x] == COLROW


def is_row(board, y, x) -> bool:
    return board[y][x] == ROW or board[y][x] == COLROW


def build_col(board, y, x) -> None:
    if board[y][x] == ROW:
        board[y][x] = COLROW
    else:
        board[y][x] = COL


def build_row(board, y, x) -> None:
    if board[y][x] == COL:
        board[y][x] = COLROW
    else:
        board[y][x] = ROW


def can_build_column(board, n, x, y) -> bool:
    # 바닥 위
    if y == 0:
        return True
    # 좌측에 보가 있는 경우
    if x - 1 >= 0 and is_row(board, y, x - 1):
        return True
    # 우측에 보가 있는 경우
    if is_row(board, y, x):
        return True
    # 다른 기둥 위
    if y - 1 >= 0 and is_col(board, y - 1, x):
        return True
    return False


def can_build_row(board, n, x, y) -> bool:
    # 좌측 끝이 기둥 위
    if y - 1 >= 0 and is_col(board, y - 1, x):
        return True
    # 우측 끝이 기둥 위
    if y - 1 >= 0 and x + 1 <= n and is_col(board, y - 1, x + 1):
        return True
    # 양쪽 끝부분이 다른 보와 동시에 연결
    if x - 1 >= 0 and is_row(board, y, x - 1):
        if x + 1 <= n and is_row(board, y, x + 1):
            return True
    return False


def can_delete_col(board, n, x, y) -> bool:
    case_a = x - 1 >= 0 and y + 1 <= n and can_build_row(board, n, x - 1, y + 1)
    case_b = y + 1 <= n and can_build_row(board, n, x, y + 1)
    case_c = y + 1 <= n and can_build_column(board, n, x, y + 1)


def solution(n: int, build_frame: list) -> list:
    board = [[-1] * (n + 1) for _ in range(n + 1)]

    for x, y, a, b in build_frame:
        # 설치하는 경우
        if b == BIL:
            # 기둥
            if a == COL:
                if can_build_column(board, n, x, y):
                    build_col(board, y, x)
            # 보
            else:
                if can_build_row(board, n, x, y):
                    build_row(board, y, x)

        # 삭제하는 경우
        else:
            # 기둥
            if a == COL:
                pass
            # 보
            else:
                pass
