"""
DFS 방식을 쓰되, 현재 맵 상태도 같이 넘겨야 함.

이때 최대 경우의 수 = 16 + 15 * 3^1 + 14 * 3^2 + 13 * 3^3 +
3^15가 대략 천만
"""

arrows = [
    (-1, 0), (-1, -1), (0, -1),
    (1, -1), (1, 0), (1, 1),
    (0, 1), (-1, 1)
]

eaten_sum = 0


def main():
    global eaten_sum

    fish_arr, dir_arr = input_fish()
    fish_order = get_fish_order(fish_arr)

    shark_pos = (0, 0)
    eaten_fish_num = fish_arr[0][0]
    fish_order[eaten_fish_num] = (-1, -1)
    eaten_sum += eaten_fish_num
    shark_dir = dir_arr[0][0]

    fish_arr_list = [fish_arr]
    for fish_arr in fish_arr_list:
        new_fish_arr = move_fish(fish_arr, fish_order)
        fish_arr_cand = move_shark(new_fish_arr, fish_order, shark_pos, shark_dir)
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


def move_fish(fish_arr, fish_order):
    pass


def get_next_pos_of_fish():
    pass


def move_shark():
    pass


main()

"""
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
"""  # 33
