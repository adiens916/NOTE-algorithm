from pathlib import Path
import sys


parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


# 상 하 좌 우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)


def dfs(row, col, diggable):
    # 길이 정보를 visited에 저장하고 불러옴
    global cur_path
    cur_path = max(cur_path, visited[row][col])

    for i in range(4):
        y = row + dy[i]
        x = col + dx[i]

        if 0 <= x < N and 0 <= y < N and not visited[y][x]:
            # 가려는 곳이 더 높은 경우
            if arr[row][col] <= arr[y][x]:
                # 처음 파는 것이고, 팠을 때 더 작아질 수 있어야 함
                if diggable and arr[y][x] - K < arr[row][col]:
                    # 기존 높이랑 경로 길이를 저장
                    origin = arr[y][x]
                    arr[y][x] = arr[row][col] - 1

                    visited[y][x] = visited[row][col] + 1    
                    dfs(y, x, False)

                    # 갔다오고 나면 높이랑 길이를 원상복구
                    arr[y][x] = origin
                    visited[y][x] = 0
            else:
                visited[y][x] = visited[row][col] + 1    
                dfs(y, x, diggable)
                visited[y][x] = 0


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 봉우리의 크기와 위치를 파악
    max_height = 0
    max_pos = []
    for row in range(N):
        for col in range(N):
            # 더 높은 곳이 있으면 기존 것을 버리고, 새로 넣기
            if arr[row][col] > max_height:
                max_height = arr[row][col]
                max_pos = []
                max_pos.append((row, col))
            elif arr[row][col] == max_height:
                max_pos.append((row, col))
            else:
                continue

    max_path = 0
    for pos in max_pos:
        cur_path = 0
        row, col = pos
        
        # 방문 체크 겸 길이 저장
        visited = [[0] * N for _ in range(N)]
        visited[row][col] = 1

        # 현재 결과를 기존 최댓값과 비교
        dfs(row, col, True)
        max_path = max(max_path, cur_path)
    
    print('#{} {}'.format(test_case, max_path))
