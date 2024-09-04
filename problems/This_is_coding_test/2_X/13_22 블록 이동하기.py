"""
(N, N)까지 이동 (두 칸 중 한 칸만 들어가면 됨)
0 = 빈칸, 1 = 벽
벽 / 지도 밖 이동 불가

앞뒤 구분없이 이동
90도 회전 가능하나, 대각선 방향 벽 없어야 함
이동 / 회전 시 1초 소요

최소 시간 반환 = BFS
방문 여부 = set?
이동해서 넣고,
회전해서 넣기
"""

from collections import deque

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def solution(board):
    N = len(board)
    # XXX: 벽(1) 두르기. 그러면 범위 벗어나는 거 검사하는 코드 중복 제거 가능.
    n_board = [[1] * (N + 2) for _ in range(N + 2)]
    for r in range(N):
        for c in range(N):
            n_board[r + 1][c + 1] = board[r][c]

    start = ((1, 1), (1, 2))
    time = 0
    visited = set()
    visited.add(start)
    queue = deque([(start, time)])
    while queue:
        start, time = queue.popleft()

        result_list1 = move(start, n_board)
        result_list2 = rotate(start, n_board)
        for next_ in (result_list1 + result_list2):
            if next_ in visited:
                continue
            visited.add(next_)

            ((r1, c1), (r2, c2)) = next_
            if n_board[r1][c1] == N or n_board[r2][c2] == N:
                return time + 1
            else:
                queue.append((((r1, c1), (r2, c2)), time + 1))


def move(start, board):
    (r1, c1), (r2, c2) = start

    result = []
    for i in range(4):
        y1 = r1 + dy[i]
        x1 = c1 + dx[i]
        y2 = r2 + dy[i]
        x2 = c2 + dx[i]

        if board[y1][x1] == 0 and board[y2][x2] == 0:
            temp = ((y1, x1), (y2, x2))
            result.append(tuple(sorted(temp)))
    return result


def rotate(start, board):
    (r1, c1), (r2, c2) = start

    # XXX: 회전 시에는 '회전 방향에만' 1이 없으면 됨
    cands = []
    if r1 == r2:  # 가로 방향
        # XXX: 위쪽이 둘 다 비어 있어야 회전 가능
        if board[r1 - 1][c1] == 0 and board[r2 - 1][c2] == 0:
            cands += [((r1, c1), (r1 - 1, c1)), ((r2 - 1, c2), (r2, c2))]
        # XXX: 아래쪽이 비어 있어야 회전 가능
        if board[r1 + 1][c1] == 0 and board[r2 + 1][c2] == 0:
            cands += [((r1, c1), (r1 + 1, c1)), ((r2 + 1, c2), (r2, c2))]
    else:  # 세로 방향
        if board[r1][c1 - 1] == 0 and board[r2][c2 - 1] == 0:
            cands += [((r1, c1), (r1, c1 - 1)), ((r2, c2 - 1), (r2, c2))]
        if board[r1][c1 + 1] == 0 and board[r2][c2 + 1] == 0:
            cands += [((r1, c1), (r1, c1 + 1)), ((r2, c2 + 1), (r2, c2))]

    result = []
    for temp in cands:
        result.append(tuple(sorted(temp)))
    return result


answer = solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
print(answer)
