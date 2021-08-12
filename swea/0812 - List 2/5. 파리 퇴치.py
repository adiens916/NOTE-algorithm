"""
처음에는 4중 반복문으로 구했는데 200ms 정도 나왔다.
다른 사람들보다 많이 나온 것 같아 DP 비슷하게 구했는데, 그래도 170ms 정도였다.

혹시나 싶어 효전님의 130ms 소스를 봤는데, 오히려 처음 구현했던 거랑 똑같았다.
단지 4중 반복문 대신에 함수를 썼다는 점이 달랐다.

: 아무래도 4중 for 보다는
함수를 이용해 for 수를 줄이는 게 좋은 듯하다.
"""

from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    length, swatter_length = map(int, input().split())
    flies = [[int(n) for n in input().split()] for _ in range(length)]

    inner_sum_list = []
    inner_sum = 0
    for row in range(swatter_length):
        for col in range(swatter_length):
            inner_sum += flies[row][col]
    inner_sum_list.append(inner_sum)

    for row in range(length - swatter_length + 1):
        for col in range(length - swatter_length + 1):
            # 열이 바뀐 경우
            if col > 0:
                inner_sum = inner_sum_list[-1]
                # 밀려난 열에 있던 값들은 지워주고
                # 새로 들어온 열에 있는 값들은 더해줌
                for inner_row in range(row, row + swatter_length):
                    inner_sum -= flies[inner_row][col - 1]
                    inner_sum += flies[inner_row][col + swatter_length - 1]
                inner_sum_list.append(inner_sum)
            # 행이 바뀐 경우
            elif row > 0:
                # 이전 행을 기준으로 하는 영역 합 가져옴
                inner_sum = inner_sum_list[-(length - swatter_length) - 1]
                # 이전 행에 있던 값들은 지워주고
                # 새로 들어온 행에 있는 값들은 더해줌
                for inner_col in range(col, col + swatter_length):
                    inner_sum -= flies[row - 1][inner_col]
                    inner_sum += flies[row + swatter_length - 1][inner_col]
                inner_sum_list.append(inner_sum)
            elif row == 0 and col == 0:
                continue
            else:
                pass
    
    max_inner_sum = 0
    for inner_sum in inner_sum_list:
        max_inner_sum = inner_sum if inner_sum > max_inner_sum else max_inner_sum

    print("#{} {}".format(test_case, max_inner_sum))

"""
T = int(input())
for test_case in range(1, T + 1):
    length, swatter_length = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(length)]
    max_inner_sum = 0

    for row in range(length - swatter_length + 1):
        for col in range(length - swatter_length + 1):
            inner_sum = 0
            for inner_row in range(row, row + swatter_length):
                for inner_col in range(col, col + swatter_length):
                    inner_sum += flies[inner_row][inner_col]
            max_inner_sum = inner_sum if inner_sum > max_inner_sum else max_inner_sum
    
    print("#{} {}".format(test_case, max_inner_sum))
"""