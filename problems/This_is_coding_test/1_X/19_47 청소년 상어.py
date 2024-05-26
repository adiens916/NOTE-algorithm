"""
DFS 방식을 쓰되, 현재 맵 상태도 같이 넘겨야 함.

이때 최대 경우의 수 = 16 + 15 * 3^1 + 14 * 3^2 + 13 * 3^3 +
3^15가 대략 천만
"""

arrows = [
    (0, 0),
    (-1, 0), (-1, -1), (0, -1),
    (1, -1), (1, 0), (1, 1),
    (0, 1), (-1, 1)
]
SHARK = 99


def main():
    fish_arr, dir_arr = input_fish()
    fish_order = get_fish_order(fish_arr)

    eaten_sum = 0
    shark_pos = (0, 0)
    eaten_fish_num = fish_arr[0][0]
    fish_order[eaten_fish_num] = (-1, -1)
    eaten_sum += eaten_fish_num
    shark_dir = dir_arr[0][0]
    fish_arr[0][0] = SHARK

    fish_arr_list = [(fish_arr, dir_arr)]
    for fish_arr, dir_arr in fish_arr_list:
        fish_order = get_fish_order(fish_arr)
        move_fish(fish_arr, dir_arr, fish_order)
        fish_arr_cand = move_shark(fish_arr, dir_arr, fish_order, shark_pos, shark_dir, eaten_sum)
        if not any(fish_arr_cand):
            print(eaten_sum)
            break
        else:
            fish_arr_list.extend(fish_arr_cand)


def input_fish():
    fish_arr = [[0] * 4 for _ in range(4)]
    dir_arr = [[0] * 4 for _ in range(4)]

    for row in range(4):
        line = list(map(int, input().split()))
        for col in range(8):
            if col % 2 == 0:
                fish_arr[row][col // 2] = line[col]
            else:
                dir_arr[row][col // 2] = line[col]

    return fish_arr, dir_arr


def get_fish_order(fish_arr: list[list[int]]) -> list[tuple[int, int]]:
    fish_order = [(-1, -1) for _ in range(17)]

    for row in range(4):
        for col in range(4):
            fish_num = fish_arr[row][col]
            fish_order[fish_num] = (row, col)

    return fish_order


def move_fish(fish_arr, dir_arr, fish_order):
    for i in range(1, 17):
        row, col = fish_order[i]
        if row == -1:
            continue

        di = dir_arr[row][col]
        n_row, n_col = get_next_pos_of_fish(fish_arr, row, col, di)

        n_fish = fish_arr[n_row][n_col]
        if n_fish > 0:
            n_di = dir_arr[n_row][n_col]
            fish_arr[row][col] = n_fish
            dir_arr[row][col] = n_di
        fish_arr[n_row][n_col] = i
        dir_arr[n_row][n_col] = di


def get_next_pos_of_fish(fish_arr, row, col, di):
    for i in range(8):
        di = (di + i) % 9
        if di == 0:
            di = 1

        n_row = row + arrows[di][0]
        n_col = col + arrows[di][1]

        if not (0 <= n_row < 4 and 0 <= n_col < 4):
            continue
        if fish_arr[n_row][n_col] == SHARK:
            continue
        return n_row, n_col


def move_shark(fish_arr, dir_arr, fish_order, shark_pos, shark_dir):
    row, col = shark_pos
    for i in range(3):
        n_row = row + arrows[shark_dir][0]
        n_col = col + arrows[shark_dir][1]

        if not (0 <= n_row < 4 and 0 <= n_col < 4):
            continue
        if fish_arr[n_row][n_col] == 0:
            continue



main()

"""
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
"""  # 33
