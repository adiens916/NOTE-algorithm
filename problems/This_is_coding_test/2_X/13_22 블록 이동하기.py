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
    start = ((0, 0), (0, 1))
    time = 0
    visited = set()
    queue = deque([(start, time)])
    while queue:
        start, time = queue.popleft()

        if start in visited:
            continue
        visited.add(start)

        result_list1 = move(start, board)
        result_list2 = rotate(start, board)
        for next_ in (result_list1 + result_list2):
            # if next_ in visited:
            #     continue
            # visited.add(next_)

            ((r1, c1), (r2, c2)) = next_
            if board[r1][c1] == N - 1 or board[r2][c2] == N - 1:
                return time + 1
            else:
                queue.append((((r1, c1), (r2, c2)), time + 1))


def move(start, board):
    (r1, c1), (r2, c2) = start
    N = len(board)

    result = []
    for i in range(4):
        y1 = r1 + dy[i]
        x1 = c1 + dx[i]
        y2 = r2 + dy[i]
        x2 = c2 + dx[i]

        is_inner1 = (0 <= y1 < N and 0 <= x1 < N)
        is_inner2 = (0 <= y2 < N and 0 <= x2 < N)
        if not (is_inner1 and is_inner2):
            continue

        if board[y1][x1] == 0 and board[y2][x2] == 0:
            temp = ((y1, x1), (y2, x2))
            result.append(tuple(sorted(temp)))
    return result


def rotate(start, board):
    (r1, c1), (r2, c2) = start
    N = len(board)

    # XXX: 회전 시에는 '회전 방향에만' 1이 없으면 됨
    if r1 == r2:  # 가로 방향
        cands = [
            ((r1, c1), (r1 - 1, c1)),
            ((r1, c1), (r1 + 1, c1)),
            ((r2 - 1, c2), (r2, c2)),
            ((r2 + 1, c2), (r2, c2))
        ]
    else:  # 세로 방향
        cands = [
            ((r1, c1), (r1, c1 - 1)),
            ((r1, c1), (r1, c1 + 1)),
            ((r2, c2 - 1), (r2, c2)),
            ((r2, c2 + 1), (r2, c2))
        ]

    result = []
    for ((y1, x1), (y2, x2)) in cands:
        is_inner1 = (0 <= y1 < N and 0 <= x1 < N)
        is_inner2 = (0 <= y2 < N and 0 <= x2 < N)
        if not (is_inner1 and is_inner2):
            continue

        if board[y1][x1] == 0 and board[y2][x2] == 0:
            temp = ((y1, x1), (y2, x2))
            result.append(tuple(sorted(temp)))
    return result


answer = solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
print(answer)
