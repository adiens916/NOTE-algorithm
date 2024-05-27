"""
DFS 방식을 쓰되, 현재 맵 상태도 같이 넘겨야 함.

이때 최대 경우의 수 = 16 + 15 * 3^1 + 14 * 3^2 + 13 * 3^3 +
3^15가 대략 천만
"""
from copy import deepcopy


SHARK = 99
dy = (0, -1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, 0, -1, -1, -1, 0, 1, 1, 1)


def main():
    fish_arr = [[[0, 0] for x in range(4)] for y in range(4)]
    for row in range(4):
        line = list(map(int, input().split()))
        for i in range(8):
            fish = line[i // 2]
            way = line[i // 2 + 1]
            fish_arr[row][i // 2] = [fish, way]

    shark_way = fish_arr[0][0][1]
    eat = 0
    shark = ([0, 0], shark_way, eat)
    fish_arr[0][0] = [SHARK, 0]

    eaten_num = dfs(fish_arr, shark)
    print(eaten_num)


def dfs(fish_arr: list[list[list[int]]], shark: tuple[list[int], int, int]) -> int:
    new_fish_arr = move_fish(fish_arr)

    pos, way, eat = shark
    for i in range(4):
        y = pos[0] + dy[way]
        x = pos[1] + dx[way]

        if not (0 <= y < 4 and 0 <= x < 4):
            continue
        if new_fish_arr[y][x][0] == 0:
            continue
        fish_arr_copy = deepcopy(new_fish_arr)


def move_fish(fish_arr):
    fish_order = get_fish_order(fish_arr)
    for i in range(1, 17):
        row, col = fish_order[i]
        fish, way = fish_arr[row][col]

        y, x = get_next_pos_of_fish(fish_arr, row, col, way)
        n_fish, n_way = fish_arr[y][x]
        if n_fish != 0:
            fish_arr[row][col] = [n_fish, n_way]
        fish_arr[y][x] = [fish, way]
    return fish_arr


def get_fish_order(fish_arr):
    fish_order = [(0, 0) for _ in range(17)]
    for row in range(4):
        for col in range(4):
            fish, way = fish_arr[row][col]
            if fish == SHARK:
                continue
            fish_order[fish] = (row, col)
    return fish_order


def get_next_pos_of_fish(fish_arr, row, col, way):
    for i in range(8):
        n_way = way + i
        if n_way == 9:
            n_way = 1

        y = row + dy[n_way]
        x = col + dx[n_way]

        if not (0 <= y < 4 and 0 <= x < 4):
            continue
        if fish_arr[y][x] == SHARK:
            continue
        return y, x


main()

"""
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
"""  # 33
