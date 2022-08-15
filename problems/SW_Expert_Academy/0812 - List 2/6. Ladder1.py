from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = 10
length = 100
for test_case in range(1, T + 1):
    test_case = int(input())
    ladder = [[int(n) for n in input().split()] for _ in range(length)]
    
    # 출발점만 찾으면 되니까, 역으로 밑에서부터 거슬러 올라가자!
    # 바닥에서 2인 곳을 찾는다.
    for col in range(length):
        if ladder[length - 1][col] == 2:
            bottom_goal = col
            break
    col = bottom_goal

    # 행 개수만큼 위로 올라간다.
    for row in range(length - 2, -1, -1):
        # 왼쪽이 1이거나 오른쪽이 1이면 그쪽으로 빠진다.
        # FIXME: Python은 -1 에 값이 있다면 마지막 원소를 가리킨다!
        # -> 값이 채워진 리스트는 일일이 범위를 지정해줘야 함
        if 0 < col and ladder[row][col - 1] == 1:
            while 0 < col and ladder[row][col - 1] == 1:
                col -= 1
        elif col < length - 1 and ladder[row][col + 1] == 1:
            while col < length - 1 and ladder[row][col + 1] == 1:
                col += 1
        else:
            # 둘 다 0이 아니면 계속 위로 올라간다.
            continue
    
    print("#{} {}".format(test_case, col))