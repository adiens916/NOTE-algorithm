from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


from collections import deque


def bfs_shortest_path(V, adj_list, start, goal):
    visited = [False] * (V + 1)

    # 시작 지점을 집어넣은 큐를 생성
    queue = deque()
    queue.append((start, 0))
    
    while queue:
        v, length = queue.popleft()

        if not visited[v]:
            visited[v] = True

            for adj_v in adj_list[v]:
                if visited[adj_v]:
                    continue
                elif adj_v == goal:
                    return length + 1
                else:
                    queue.append((adj_v, length + 1))
    
    # 도착하지 못한 경우 0을 반환
    return 0


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    # 인접 리스트 형태로 구현
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        v_in, v_out = map(int, input().split())
        adj_list[v_in].append(v_out)
        adj_list[v_out].append(v_in)
    
    start, goal = map(int, input().split())

    # 최단 경로 길이 찾기
    result = bfs_shortest_path(V, adj_list, start, goal)
    print("#{} {}".format(test_case, result))
