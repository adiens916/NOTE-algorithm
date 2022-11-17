import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline

BW_BOARD = ["BWBWBWBW", "WBWBWBWB"] * 4
WB_BOARD = ["WBWBWBWB", "BWBWBWBW"] * 4


def main():
    N, M = map(int, input().split())
    board = [input().rstrip() for _ in range(N)]
    min_diff = N * M

    for row in range(N - 7):
        for col in range(M - 7):
            diff_by_bw_board = count_diff(board, row, col, BW_BOARD)
            diff_by_wb_board = count_diff(board, row, col, WB_BOARD)
            diff = min(diff_by_bw_board, diff_by_wb_board)
            min_diff = min(diff, min_diff)

    print(min_diff)


def count_diff(board: list[str], row: int, col: int, pattern: list[str]):
    diff = 0

    for i in range(8):
        for j in range(8):
            if pattern[i][j] != board[row + i][col + j]:
                diff += 1

    return diff


main()
