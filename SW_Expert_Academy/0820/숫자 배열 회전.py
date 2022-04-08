from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def rotate(arr):
    arr_90 = [row[:] for row in arr]
    N = len(arr_90)
    middle = (N - 1) // 2
    
    # FIXME: middle 까지 -> +1을 해줘야 함
    for n in range(middle + 1):
        # FIXME: 양쪽 간격이 줄어듦 -> -2씩
        # -> 간격을 그리자
        for diff in range(N - 1 - n * 2):
            left_top = arr_90[n][n + diff]
            right_top = arr_90[n + diff][N - 1 - n]
            right_bottom = arr_90[N - 1 - n][N - 1 - n - diff]
            left_bottom = arr_90[N - 1 - n - diff][n]

            arr_90[n][n + diff] = left_bottom
            arr_90[n + diff][N - 1 - n] = left_top
            arr_90[N - 1 - n][N - 1 - n - diff] = right_top
            arr_90[N - 1 - n - diff][n] = right_bottom
    
    return arr_90


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr_90 = rotate(arr)
    arr_180 = rotate(arr_90)
    arr_270 = rotate(arr_180)

    print("#{}".format(test_case))
    for i in range(N):
        print(*arr_90[i], sep="", end=" ")
        print(*arr_180[i], sep="", end=" ")
        print(*arr_270[i], sep="", end=" ")
        print()
