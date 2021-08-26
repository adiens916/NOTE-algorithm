from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


from collections import deque


# 의미 있는 값으로 표시
WALL = '1'
START = '2'
GOAL = '3'


def get_start(arr):
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if arr[row][col] == START:
                return row, col


def bfs_shortest_path(maze, start):
    # 상하좌우 방향의 오프셋들
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)

    # 시작 지점을 집어넣은 큐를 생성
    queue = deque([start])
    
    while queue:
        # 행, 열, 현재까지의 경로 길이
        row, col = queue.popleft()
        # 벽이 아닐 때만 진행
        if maze[row][col] != WALL:
            maze[row][col] = WALL

            for i in range(4):
                adj = maze[row + dy[i]][col + dx[i]]
                # 다음이 벽인 곳은 넘김
                if adj == WALL:
                    continue
                # 다음이 도착 지점이면 1 반환
                elif adj == GOAL:
                    return 1
                # 다음 지점의 정보를 큐에 집어넣음
                else:
                    queue.append((row + dy[i], col + dx[i]))
    
    # 도착하지 못한 경우 0을 반환
    return 0


T = 10
N = 100
for test_case in range(1, T + 1):
    input()
    arr = [list(input()) for _ in range(N)]
    
    # 시작 지점 찾기
    start = get_start(arr)
    # 최단 경로 길이 찾기
    result = bfs_shortest_path(arr, start)
    print("#{} {}".format(test_case, result))
