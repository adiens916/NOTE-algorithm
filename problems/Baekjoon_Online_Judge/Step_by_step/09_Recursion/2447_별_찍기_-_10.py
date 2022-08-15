import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


# 배열 만들고, 배열 내용 바꾸기
# 시간 복잡도는 O(N^3)
def solution2():
    def remove_center(arr: list[list[str]], row_start, col_start, N):
        length = N // 3

        for row in range(row_start + length, row_start + length * 2):
            for col in range(col_start + length, col_start + length * 2):
                arr[row][col] = ' '
        
        if length == 1:
            return

        for row in range(row_start, row_start + length * 2 + 1, length):
            for col in range(col_start, col_start + length * 2 + 1, length):
                remove_center(arr, row, col, length)


    N = int(input())
    arr = [['*'] * N for _ in range(N)]
    remove_center(arr, 0, 0, N)

    for row in range(N):
        print(*arr[row], sep='')


# 각 좌표마다 재귀로 판단
def solution1():
    def get_scaled_value(N, row, col):
        # 종료 조건은 N이 3일 때,
        if N == 3:
            # 가운데 부분의 좌표인 경우 빈 값
            if row == 1 and col == 1:
                return ' '
            # 가운데 이외는 *
            else:
                return '*'
        else:
            # 현재보다 더 작은 단위 계산
            scale = N // 3
            
            # 더 작은 단위에서 봤을 때 가운데 부분이면 빈 값
            if row // scale == 1 and col // scale == 1:
                return ' '
            # 가운데 부분이 아니면
            else:
                # 단위를 한 번 더 줄이면서 
                # 가운데인지 아닌지 계속 판단
                return get_scaled_value(
                    scale, 
                    row % scale, 
                    col % scale
                )


    N = int(input())
    for row in range(0, N):
        for col in range(0, N):
            print(get_scaled_value(N, row, col), end='')
        print()
