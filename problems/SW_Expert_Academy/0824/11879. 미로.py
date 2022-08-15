from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
# input = sys.stdin.readline


def find_start(arr, N):
    for y in range(N):
        for x in range(N):
            if arr[y][x] == '2':
                return y, x


def dfs(arr, start):
    move_set = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    stack = [start]
    N = len(arr)

    while stack:
        row, col = stack.pop()
        if arr[row][col] != '1':
            arr[row][col] = '1'

            for move in move_set:
                y, x = move
                # FIXME: 범위는 0을 포함해야 함
                if 0 <= row + y < N and 0 <= col + x < N:
                    nxt = arr[row + y][col + x]
                    if nxt == '1':
                        continue
                    if nxt == '3':
                        return 1
                    stack.append((row + y, col + x))

    return 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    start = find_start(arr, N)
    result = dfs(arr, start)
    print("#{} {}".format(test_case, result))
