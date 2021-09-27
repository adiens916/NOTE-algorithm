from pathlib import Path
import sys


parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
BFS + 동시에 출발!
: '물'에서부터 뻗어나가며, 
뻗어온 거리를 모든 '땅'에다 저장
"""


from collections import deque


# 상하좌우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    queue = deque()

    for row in range(N):
        for col in range(M):
            if arr[row][col] == 'W':
                visited[row][col] = 1
                queue.append((row, col))
    
    movement_sum = 0
    while queue:
        row, col = queue.popleft()
        movement_sum += visited[row][col]

        for i in range(4):
            y = row + dy[i]
            x = col + dx[i]

            # 범위 체크
            if 0 <= y < N and 0 <= x < M:
                # 방문 체크
                if visited[y][x]:
                    continue
                # 주변 탐색
                else:
                    visited[y][x] = visited[row][col] + 1
                    queue.append((y, x))

    movement_sum -= N * M
    print('#{} {}'.format(test_case, movement_sum))
