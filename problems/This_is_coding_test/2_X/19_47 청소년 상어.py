"""
4x4 x,y
물고기 번호 & 방향
번호 1~16
방향 8가지

1. 먹음. 방향 복사함.
2. 물고기 이동.
    작은 번호부터 이동.
    이동 가능할 때까지 45도씩 반시계 회전
3. 상어 이동.
    이때, 경우의 수가 나뉨. -> DFS
    못 먹으면 종료
먹은 물고기 최댓값 구하기
"""

arr = [[(0, 0)] * 4 for _ in range(4)]
for row in range(4):
    line = list(map(int, input().split()))
    for col in range(4):
        fish = line[2 * col]
        direct = line[2 * col + 1] - 1  # 1부터 시작이므로 줄이기
        arr[row][col] = (fish, direct)

dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, -1, -1, -1, 0, 1, 1, 1)
max_eaten = 0


def move_fish(arr, shark_y, shark_x):
    index_list = [(-1, -1) for _ in range(17)]
    for row in range(4):
        for col in range(4):
            fish = arr[row][col][0]
            if fish > 0:
                index_list[fish] = (row, col)

    for num in range(1, 17):
        row, col = index_list[num]
        if row == -1:
            continue

        # XXX: 원래 갖고 있던 방향 기준으로 먼저 체크 필요.
        fish, direct = arr[row][col]
        for i in range(8):
            new_direct = (direct + i) % 8
            y = row + dy[new_direct]
            x = col + dx[new_direct]

            if not (0 <= y < 4 and 0 <= x < 4):
                continue
            if y == shark_y and x == shark_x:
                continue

            n_fish, n_direct = arr[y][x]
            arr[y][x] = (fish, new_direct)
            arr[row][col] = (n_fish, n_direct)

            index_list[num] = (y, x)
            index_list[n_fish] = (row, col)
            break

    # XXX: return 문 들여쓰기 잘못함.
    # 아예 함수 시작부터 return문 써놓기.
    return arr


def dfs(row, col, eaten, arr):
    global max_eaten
    fish, direct = arr[row][col]
    eaten += fish
    max_eaten = max(max_eaten, eaten)
    arr[row][col] = (0, -1)

    arr = move_fish(arr, row, col)

    # XXX: 범위가 3이 아니라 4까지 가야 함. 그래야 3칸까지 감.
    # 방금 먹은 곳은 굳이 체크할 필요가 없긴 하니, 1부터 시작해도 됨.
    for i in range(1, 4):
        y = row + dy[direct] * i
        x = col + dx[direct] * i

        if (0 <= y < 4 and 0 <= x < 4) and arr[y][x][0] > 0:
            # deepcopy 대신에 슬라이싱 활용 (20ms 단축)
            new_arr = [line[:] for line in arr]
            dfs(y, x, eaten, new_arr)
        # XXX: 완전 새 복사본을 넘기므로, 이전으로 복구할 필요없음.
        # eaten_sum -= fish
        # arr[y][x] = (fish, direct)


dfs(0, 0, 0, arr)
print(max_eaten)
