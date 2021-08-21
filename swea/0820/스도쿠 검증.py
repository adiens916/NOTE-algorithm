from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def check_rows(arr):
    for i in range(9):
        num_set = set()
        for j in range(9):
            num_set.add(arr[i][j])
        if len(num_set) != 9:
            return 0
    return 1


def check_cols(arr):
    for i in range(9):
        num_set = set()
        for j in range(9):
            num_set.add(arr[j][i])
        if len(num_set) != 9:
            return 0
    return 1


def check_area(arr):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            num_set = set()
            for y in range(3):
                for x in range(3):
                    num_set.add(arr[i + y][j + x])
            if len(num_set) != 9:
                return 0
    return 1


def check_validity(arr):
    return check_rows(arr) and check_cols(arr) and check_area(arr)


T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = check_validity(arr)
    print("#{} {}".format(test_case, result))
