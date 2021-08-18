from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def pascal_triangle(N):
    # N * N 만큼의 2차원 배열을 만든다.
    arr = [[0] * N for row in range(N)]

    for row in range(N):
        for col in range(row + 1):
            # 맨 앞과 뒤는 1로 채운다.
            if col == 0 or col == row:
                arr[row][col] = 1
            
            # [이전 행][이전 열] + [이전 행][지금 열]
            # = [지금 행][지금 열]
            else:
                arr[row][col] = arr[row - 1][col - 1] + arr[row - 1][col]

    return arr


T = int(input())
for test_case in range(1, T + 1):
    print("#{}".format(test_case))
    
    N = int(input())
    arr = pascal_triangle(N)
    
    for row in arr:
        for col in row:
            if col:
                print(col, end=" ")
        print()