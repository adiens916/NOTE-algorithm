from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


import heapq


INF = 1 << 30
# 상하좌우
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def short_path_dijkstra(row, col):
    # 비용들을 무한대로 설정하고, 시작점만 0으로 초기화.
    C = [[INF] * N for _ in range(N)]
    C[row][col] = 0

    # 힙 생성 후, 시작점 넣어줌.
    H = []
    heapq.heappush(H, (0, row, col))

    # 힙 반복
    while H:
        cost, row, col = heapq.heappop(H)

        # 해당 지점 비용이 힙에 들어갈 때보다 더 낮아질 때도 있음.
        # <- 이미 한 번 들러서 갱신된 것.
        # 아무튼 더 높으면 그 방향으로 갈 필요없으므로 패스.
        if cost > C[row][col]:
            continue
        
        # 상하좌우 이동
        for i in range(4):
            y = row + dy[i]
            x = col + dx[i]
            # 범위 체크
            if 0 <= x < N and 0 <= y < N:
                # 높이 차이에 따른 비용 계산
                diff = arr[y][x] - arr[row][col]
                cost = diff + 1 if diff > 0 else 1
                # 비용 비교
                if C[y][x] > C[row][col] + cost:
                    C[y][x] = C[row][col] + cost
                    heapq.heappush(H, (C[y][x], y, x))
    
    # 마지막 지점까지 가는 최소 비용 반환
    return C[N - 1][N - 1]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_cost = short_path_dijkstra(0, 0)
    
    print('#{} {}'.format(test_case, min_cost))
