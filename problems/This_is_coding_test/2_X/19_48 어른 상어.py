"""
1~M까지.
맨 처음 냄새 뿌림.
1초마다 이동. (i)
이동 후 냄새 사라짐 (k번 이동 시 사라짐.)
새로 냄새 뿌림.

(i-1) 이동 시,
1. 아무 냄새가 없는 칸
    -> 2차원 배열로 따로 관리해서, 바로 참조할 수 있게
2. 없으면, 자신의 냄새가 있는 칸
3. 우선순위에 따름
    상어마다 다름, 방향에 따라 다름.

(i-2) 이동 후,
한 칸에 여러 상어가 있을 시, 작은 것만 남음.
    -> 이동하고, 냄새가 0인 곳이면 새로 이동한 것이므로, 낮은 것만 놓기.
"""

# 입력
N, M, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
directs = [0] + list(map(int, input().split()))
directs = [direct - 1 for direct in directs]

priors = [[]]
for _ in range(M):
    direct_for_shark = []
    for i in range(4):
        # 순회 시 편의를 위해, 0부터 시작하게 만들기
        d1, d2, d3, d4 = map(int, input().split())
        direct_for_shark.append((d1 - 1, d2 - 1, d3 - 1, d4 - 1))
    priors.append(direct_for_shark)

# XXX: 복사 방식 틀림
odor_nums = [line[:] for line in arr]
odor_counts = [[0] * N for _ in range(N)]

sharks = []
for row in range(N):
    for col in range(N):
        if arr[row][col] > 0:
            shark = arr[row][col]
            sharks.append((shark, row, col, directs[shark]))
            # 맨 처음 냄새 뿌림
            odor_counts[row][col] = k

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def is_no_odor_around(row, col):
    for i in range(4):
        y = row + dy[i]
        x = col + dx[i]

        if not (0 <= y < N and 0 <= x < N):
            continue

        # XXX: 조건 만족이 하나라도 있으면 참 반환.
        if odor_nums[y][x] == 0:
            return True

    return False


def move():
    new_sharks = []
    for shark, row, col, direct in sharks:
        # 3. 우선순위에 따름
        #     상어마다 다름, 방향에 따라 다름.
        prior_for_shark = priors[shark][direct]

        # 1. 아무 냄새가 없는 칸
        if is_no_odor_around(row, col):
            for d in prior_for_shark:
                y = row + dy[d]
                x = col + dx[d]

                if not (0 <= y < N and 0 <= x < N):
                    continue

                # 냄새가 0인 곳이면 새로 이동 가능
                # XXX: 조건 복잡하니 나누기
                if odor_nums[y][x] > 0:
                    continue

                # 처음 들어가거나, 한 칸에 여러 상어가 있을 시, 작은 것만 남음.
                if arr[y][x] == 0 or shark < arr[y][x]:
                    new_sharks.append((shark, y, x, d))
                    # XXX: 바로 arr에도 반영했어야 함.
                    arr[y][x] = shark
                # XXX: 쫓겨남.
                else:
                    pass
                # XXX: 이동하거나 쫓겨났으므로 종료.
                break

        # 2. 없으면, 자신의 냄새가 있는 칸
        else:
            for d in prior_for_shark:
                y = row + dy[d]
                x = col + dx[d]

                if not (0 <= y < N and 0 <= x < N):
                    continue

                if odor_nums[y][x] == shark:
                    new_sharks.append((shark, y, x, d))
                    # XXX: 여기다가도 상어 추가
                    arr[y][x] = shark
                    break

    # 움직인 (살아남은) 상어들만 반환
    return new_sharks


for t in range(1001):
    if len(sharks) == 1:
        print(t)
        break
    # 1초마다 이동.
    new_sharks = move()

    # 이동 후 냄새 사라짐 (k번 이동 시 사라짐.)
    for row in range(N):
        for col in range(N):
            if odor_counts[row][col] > 0:
                odor_counts[row][col] -= 1
                if odor_counts[row][col] == 0:
                    odor_nums[row][col] = 0

    # 이전 위치 제거
    for shark, row, col, d in sharks:
        arr[row][col] = 0
    # 새로 냄새 뿌림.
    for shark, row, col, d in new_sharks:
        odor_nums[row][col] = shark
        odor_counts[row][col] = k

    sharks = new_sharks

if len(sharks) > 1:
    print(-1)

"""
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
"""