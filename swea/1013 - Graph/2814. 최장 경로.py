from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def dfs(s, cur_len):
    global max_len

    # 들어가고 나서 방문 체크
    visited[s] = True

    has_candidates = False
    for v in graph[s]:
        # 방문 체크
        if not visited[v]:
            # 방문할 게 있음.
            has_candidates = True
            # 방문할 게 있으면 들어가기.
            dfs(v, cur_len + 1)
    # FIXME: '현재 지점'에서 더 이상 갈 곳 없었으면 종료
    if not has_candidates:
        if cur_len > max_len:
            max_len = cur_len

    # 되돌아가기 전에 방문 해제
    visited[s] = False


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    # 1부터 N개까지의 인접 리스트
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    # 최대 길이 = 정점 개수
    max_len = 0

    # 방문 체크 배열. 
    visited = [False] * (N + 1)
    
    # 각 정점마다 최대 길이 찾기
    for v in range(1, N + 1):
        dfs(v, 1)
    
    print('#{} {}'.format(test_case, max_len))
