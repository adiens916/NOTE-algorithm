from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


for test_case in range(10):
    test_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    
    # 행 최대합
    for row in range(100):
        row_sum = 0
        for col in range(100):
            row_sum += arr[row][col]
        if row_sum > max_sum:
            max_sum = row_sum

    # 열 최대합
    for col in range(100):
        col_sum = 0
        for row in range(100):
            col_sum += arr[row][col]
        if col_sum > max_sum:
            max_sum = col_sum

    # 오른쪽 아래 대각선 최대합
    diagonal_sum = 0
    for n in range(100):
        diagonal_sum += arr[n][n]
    if diagonal_sum > max_sum:
            max_sum = diagonal_sum

    # 왼쪽 아래 대각선 최대합
    diagonal_sum = 0
    for n in range(100):
        diagonal_sum += arr[n][99 - n]
    if diagonal_sum > max_sum:
            max_sum = diagonal_sum

    print("#{} {}".format(test_num, max_sum))
