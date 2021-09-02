from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
# input = sys.stdin.readline


stations = {"A": 1, "B": 2, "C": 3}
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def change_adjacency(row, col):
    scope = stations[arr[row][col]]
    for s in range(1, scope + 1):
        for i in range(4):
            # 살펴보려는 곳의 좌표
            y = row + dy[i] * s
            x = col + dx[i] * s

            # 좌표가 범위를 벗어나면 넘김
            if y < 0 or y > N - 1:
                continue
            if x < 0 or x > N - 1:
                continue

            # 집일 때만 X로 바꾸기
            # 다른 기지국은 놔두기
            if arr[y][x] == "H":
                arr[y][x] = "X"


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if arr[y][x] in stations:
                change_adjacency(y, x)
    
    count = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] == "H":
                count += 1

    print("#{} {}".format(test_case, count))
