"""
DFS 방식을 쓰되, 현재 맵 상태도 같이 넘겨야 함.

이때 최대 경우의 수 = 16 + 15 * 3^1 + 14 * 3^2 + 13 * 3^3 +
3^15가 대략 천만
"""
from copy import deepcopy


max_eaten_fish = 0
dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, -1, -1, -1, 0, 1, 1, 1)


def main():
    fish_arr = [[[0, 0] for x in range(4)] for y in range(4)]
    for row in range(4):
        line = list(map(int, input().split()))
        # XXX: 입력이 잘 됐는지부터 체크하기...
        for col in range(4):
            fish = line[col * 2]
            way = line[col * 2 + 1] - 1
            fish_arr[row][col] = [fish, way]

    shark = (0, 0)
    dfs(fish_arr, shark, 0)
    print(max_eaten_fish)


def dfs(fish_arr: list[list[list[int]]], shark: tuple[int, int], total_eat: int) -> None:
    global max_eaten_fish

    s_row, s_col = shark
    total_eat += eat_fish(fish_arr, s_row, s_col)
    move_all_fish(fish_arr, s_row, s_col)

    # XXX: 후보 구하기 & 더 이상 후보 없으면 종료
    candidates = get_fish_candidates(fish_arr, s_row, s_col)
    if len(candidates) == 0:
        # XXX: 현재 최대 vs. 이번 분기까지 넘어온 값 비교
        max_eaten_fish = max(max_eaten_fish, total_eat)
        return
    for y, x in candidates:
        new_arr = deepcopy(fish_arr)
        # 다음 분기로 값 넘기기
        dfs(new_arr, (y, x), total_eat)


def eat_fish(fish_arr, row, col) -> int:
    fish = fish_arr[row][col][0]
    fish_arr[row][col][0] = -1
    return fish


def move_all_fish(fish_arr, s_row, s_col):
    for i in range(1, 17):
        # XXX: 물고기 위치가 계속 바뀌니까, 그냥 매번 찾는 게 더 쉬움.
        row, col = find_fish(fish_arr, i)
        # 해당 번호가 없으면 넘어감.
        if row == -1:
            continue
        fish, way = fish_arr[row][col]

        # 다음에 갈 수 있는 곳 찾기
        # XXX: 방향 바뀐 걸로 쓰기
        y, x, way = get_next_pos_way_of_fish(row, col, way, s_row, s_col)
        # 서로 위치 바꾸기
        n_fish, n_way = fish_arr[y][x]
        fish_arr[y][x] = [fish, way]
        fish_arr[row][col] = [n_fish, n_way]


def find_fish(fish_arr, i):
    for row in range(4):
        for col in range(4):
            if fish_arr[row][col][0] == i:
                return row, col
    # XXX: 이미 먹어서 없는 경우도 고려
    return -1, -1


def get_next_pos_way_of_fish(row, col, way, s_row, s_col):
    for i in range(8):
        # XXX: 로테이션은 더하기로 하면 실수하니까, 그냥 나머지 연산으로 구하기
        n_way = (way + i) % 8

        y = row + dy[n_way]
        x = col + dx[n_way]

        if not (0 <= y < 4 and 0 <= x < 4):
            continue
        # XXX: 상어인지는 좌표 '값' 대신에 그냥 좌표로 비교하는 게 제일 쉬움
        # 좌표 '값'으로 비교하면, 상어가 옮겨 다닐 떄마다 좌표 값을 갱신해야 해서 매우 복잡해짐.
        if y == s_row and x == s_col:
            continue

        # XXX: 방향 바뀌니까, 방향도 반환하기
        return y, x, n_way


def get_fish_candidates(fish_arr, s_row, s_col):
    s_way = fish_arr[s_row][s_col][1]

    cand = []
    for i in range(4):
        # XXX: 1씩 늘려 가야 함
        s_row += dy[s_way]
        s_col += dx[s_way]

        if not (0 <= s_row < 4 and 0 <= s_col < 4):
            continue
        if fish_arr[s_row][s_col][0] == -1:
            continue
        cand.append((s_row, s_col))
    return cand


main()

"""
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
"""  # 33
"""
16 7 1 4 4 3 12 8
14 7 7 6 3 4 10 2
5 2 15 2 8 3 6 4
11 8 2 4 13 5 9 4
"""  # 43
"""
12 6 14 5 4 5 6 7
15 1 11 7 3 7 7 5
10 3 8 3 16 6 1 1
5 8 2 7 13 6 9 2
"""  # 76
"""
2 6 10 8 6 7 9 4
1 7 16 6 4 2 5 8
3 7 8 6 7 6 14 8
12 7 15 4 11 3 13 3
"""  # 39
