from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


import heapq


INF = 1 << 30


def short_path_dijkstra(s):
    # 비용들을 무한대로 설정하고, 시작점만 0으로 초기화.
    C = [INF] * (N + 1)
    C[s] = 0

    # 힙 생성 후, 시작점 넣어줌.
    H = []
    heapq.heappush(H, (0, s))

    # 힙 반복
    while H:
        cost, s = heapq.heappop(H)

        # 해당 지점 비용이 힙에 들어갈 때보다 더 낮아질 때도 있음.
        # <- 이미 한 번 들러서 갱신된 것.
        # 아무튼 더 높으면 그 방향으로 갈 필요없으므로 패스.
        if cost > C[s]:
            continue
        
        # 인접점
        for v, cost in W[s]:
            # 비용 비교
            if C[v] > C[s] + cost:
                C[v] = C[s] + cost
                heapq.heappush(H, (C[v], v))
    
    # 마지막 지점까지 가는 최소 비용 반환
    return C[N]


T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    
    W = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        W[s].append((e, w))
    
    min_cost = short_path_dijkstra(0)
    
    print('#{} {}'.format(test_case, min_cost))
