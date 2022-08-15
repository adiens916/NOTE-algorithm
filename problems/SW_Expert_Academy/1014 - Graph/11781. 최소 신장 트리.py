from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
MST => Prim 알고리즘
1. 시작점 가중치 0
2. 최소 가중치로 연결된 정점 가져오기
3. 해당 정점과 연결된 정점들의 가중치 갱신
"""

import heapq


def mst_prim(s):
    T = [False] * (V + 1)
    C = [INF] * (V + 1)
    C[s] = 0
    
    H = []
    heapq.heappush(H, (0, s))

    while H:
        _, s = heapq.heappop(H)
        T[s] = True

        for v, cost_s_to_v in W[s]:
            if not T[v]:
                if C[v] > cost_s_to_v:
                    C[v] = cost_s_to_v
                    heapq.heappush(H, (C[v], v))
    
    return sum(C)


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    W = [[] for _ in range(V + 1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        W[n1].append((n2, w))
        W[n2].append((n1, w))
    
    INF = 1 << 30
    total = mst_prim(0)

    print('#{} {}'.format(test_case, total))
