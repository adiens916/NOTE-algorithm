# pillar board와 beam board를 따로 만들어서 풀 수 있다. 그러면 서로 겹쳐도 됨.
# 삭제 후 가능 여부는, 그냥 answer를 한번 돌면서 전부 체크하면 된다.
# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/60061/solution_groups?language=python3


def is_installable(x, y, is_beam, beam_board, pillar_board):
    if is_beam:
        return (pillar_board[x][y - 1] or pillar_board[x + 1][y - 1]) or (
            (x >= 1 and beam_board[x - 1][y]) and beam_board[x + 1][y]
        )
    else:
        return (
            (y == 0)
            or ((x >= 1 and beam_board[x - 1][y]) or beam_board[x][y])
            or pillar_board[x][y - 1]
        )


def install(x, y, is_beam, beam_board, pillar_board, is_install):
    if is_beam:
        beam_board[x][y] = is_install
    else:
        pillar_board[x][y] = is_install


def check_validity(res, beam_board, pillar_board):
    for x, y, is_beam in res:
        if not is_installable(x, y, is_beam, beam_board, pillar_board):
            return False
    return True


def solution(board_sz, insts):
    res = []
    beam_board = [[False] * (board_sz + 1) for _ in range(board_sz + 1)]
    pillar_board = [[False] * (board_sz + 1) for _ in range(board_sz + 1)]
    for x, y, is_beam, is_install in insts:
        if is_install:
            if is_installable(x, y, is_beam, beam_board, pillar_board):
                install(x, y, is_beam, beam_board, pillar_board, is_install)
                res.append([x, y, is_beam])
        else:
            install(x, y, is_beam, beam_board, pillar_board, is_install)
            if check_validity(res, beam_board, pillar_board):
                res.remove([x, y, is_beam])
            else:
                install(x, y, is_beam, beam_board, pillar_board, True)
    return sorted(res)
