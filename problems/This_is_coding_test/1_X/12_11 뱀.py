from collections import deque


BLANK = 0
BODY = 1
APPLE = 2


N = int(input())  # 보드 크기
board = [[BLANK] * (N + 1) for _ in range(N + 1)]

K = int(input())  # 사과 개수
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = APPLE

L = int(input())  # 방향 변환 횟수
d_changes = deque([])
for _ in range(L):
    X, C = input().split()
    d_changes.append((int(X), C))


# 게임이 몇 초에 끝나는가?
time = 0

# 초기 설정
snake = deque([(1, 1)])
board[1][1] = 1

d_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상
d_idx = 0


while True:
    time += 1

    # 다음에 머리가 오는 곳 확인
    head = snake[-1]
    dr = d_list[d_idx][0]
    dc = d_list[d_idx][1]

    r = head[0] + dr
    c = head[1] + dc

    # 다음에 머리가 오는 곳이 벽이면 종료
    if not (1 <= r <= N and 1 <= c <= N):
        break
    # 자기 몸이면 종료
    if board[r][c] == BODY:
        break

    # 한 칸 진행
    snake.append((r, c))
    # 사과가 "없으면" 꼬리 줄이기
    # XXX: 먼저 BODY로 채우면 사과 있는지 확인 불가 ⇒ 사과부터 체크
    if board[r][c] != APPLE:
        # XXX: popleft로 지우기
        tail_r, tail_c = snake.popleft()
        board[tail_r][tail_c] = BLANK
    # XXX: 사과가 있든 없든 상관없이 무조건 몸 위치함.
    board[r][c] = BODY

    # XXX: 방향 전환 횟수 남았는지 확인 필요
    if len(d_changes) == 0:
        continue

    # X초가 끝난 뒤 방향 전환
    X, C = d_changes[0]
    if X == time:
        d_changes.popleft()
        if C == "D":
            d_idx = (d_idx + 1) % 4
        elif C == "L":
            d_idx = (d_idx - 1) % 4


print(time)

"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
"""  # 9
"""
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
"""  # 21
"""
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
"""  # 13
