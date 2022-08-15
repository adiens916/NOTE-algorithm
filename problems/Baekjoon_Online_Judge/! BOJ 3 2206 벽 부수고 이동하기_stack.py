from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name.rsplit('_')[0]}.txt")
input = sys.stdin.readline


# 이동 방향: 상 하 좌 우
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

# 전체 맵을 DFS 방식으로 순회
def dfs():
    global shortest_len
    stack = [(0, 0, True, 1)]

    while stack:
        row, col, breakable, cur_len = stack.pop() 
    
        # 방문 체크
        if used[row][col]:
            continue
        # 가지치기
        if cur_len > shortest_len:
            continue
        # 종료 조건
        if row == N - 1 and col == M - 1:
            shortest_len = cur_len
            continue

        # 방문 표시
        used[row][col] = True

        for i in range(4):
            y = row + dy[i]
            x = col + dx[i]

            # 범위 체크
            if not (0 <= x < M and 0 <= y < N):
                continue
            
            # 이동할 수 있는 곳이면 그냥 이동
            if arr[y][x] == 0:
                stack.append((y, x, breakable, cur_len + 1))
            # 벽인데 부술 수 있으면, 기회 소모하고 이동
            elif breakable:
                stack.append((y, x, False, cur_len + 1))
            # 벽인데 부술 수 없으면 중단
            else:
                continue            
        
        # 다른 경로를 위해 방문 표시 풀어주기
        used[row][col] = False


N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

used = [[False] * M for _ in range(N)]

shortest_len = N * M
dfs()

if shortest_len != N * M:
    print(shortest_len)
else:
    print(-1)
