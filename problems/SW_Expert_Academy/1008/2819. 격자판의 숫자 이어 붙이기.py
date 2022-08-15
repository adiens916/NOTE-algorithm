from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


# 상 하 좌 우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

T = int(input())
for test_case in range(1, T + 1):
    N = 4
    arr = [list(map(int, input().split())) for _ in range(N)]
    number_set = set()

    # BFS
    stack = [(row, col, 0, arr[row][col]) for row in range(N) for col in range(N)]
    while stack:
        row, col, length, number = stack.pop()
        for i in range(4):
            y = row + dy[i]
            x = col + dx[i]
            if 0 <= x < 4 and 0 <= y < 4:
                new_number = number * 10 + arr[y][x]
                if length == 5:
                    number_set.add(new_number)
                else:
                    stack.append((y, x, length + 1, new_number))

    print(f'#{test_case} {len(number_set)}')
