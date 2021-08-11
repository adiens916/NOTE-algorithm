from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def abs_val(a, b):
    return a - b if a - b > 0 else b - a


move_x = (0, 0, -1, 1)
move_y = (-1, 1, 0, 0)
direction = ("up", "down", "left", "right")
move = {d: {"x": move_x[i], "y": move_y[i]} for i, d in enumerate(direction)}
# print(move)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    adjacent_sum = 0

    for row in range(N):
        for col in range(N):
            for i in range(4):
                d_x = move_x[i]
                d_y = move_y[i]
                if 0 <= row + d_x < N and 0 <= col + d_y < N:
                    adjacent_val = board[row + d_x][col + d_y]
                    base_val = board[row][col]
                    adjacent_sum += abs_val(base_val, adjacent_val)

    print("#{} {}".format(test_case, adjacent_sum))
