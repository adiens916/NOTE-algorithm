N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
directs = list(map(int, input().split()))
priors = []
for _ in range(M):
    p_for_shark = [list(map(int, input().split())) for _ in range(4)]
    priors.append(p_for_shark)

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

odor_nums = [[0] * N for _ in range(N)]
odor_counts = [[0] * N for _ in range(N)]


def update_smell():
    for row in range(N):
        for col in range(N):
            if odor_counts[row][col] > 0:
                odor_counts[row][col] -= 1
                if odor_counts[row][col] == 0:
                    odor_nums[row][col] = 0
            if arr[row][col] > 0:
                odor_nums[row][col] = arr[row][col]
                odor_counts[row][col] = K


def move():
    new_arr = [[0] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if arr[row][col] == 0:
                continue

            shark = arr[row][col]
            d = directs[shark - 1]
            ps = priors[shark - 1][d - 1]

            is_moved = False
            for d in ps:
                y = row + dy[d - 1]
                x = col + dx[d - 1]

                if not (0 <= y < N and 0 <= x < N):
                    continue

                if odor_nums[y][x] != 0:
                    continue

                is_moved = True
                if new_arr[y][x] == 0 or shark < new_arr[y][x]:
                    new_arr[y][x] = shark
                    directs[shark - 1] = d
                # XXX: 일단 이동했으므로 살아남든 쫓겨나든 종료해야 함.
                # 계속 실수하니까, 쫓겨나는 경우도 눈에 띄게 처리해주기.
                else:
                    pass
                break

            if is_moved:
                continue

            for d in ps:
                y = row + dy[d - 1]
                x = col + dx[d - 1]

                if not (0 <= y < N and 0 <= x < N):
                    continue

                if odor_nums[y][x] == shark:
                    new_arr[y][x] = shark
                    directs[shark - 1] = d
                    break

    return new_arr


def is_only_one_left():
    for row in range(N):
        for col in range(N):
            if arr[row][col] > 1:
                return False
    return True


result = -1
# XXX: 처음부터 이동 못 하는 경우는 없다.
for t in range(1, 1001):
    update_smell()
    new_arr = move()
    arr = new_arr

    if is_only_one_left():
        result = t
        break

print(result)
