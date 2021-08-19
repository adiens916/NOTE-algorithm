from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def input_matrix(V, E):
    adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        v_in, v_out = map(int, input().split())
        # 방향 그래프이므로, 한쪽으로만 체크
        adj_matrix[v_in][v_out] = 1
    return adj_matrix


def dfs_path_check(matrix, start, goal):
    vertex_num = len(matrix) - 1
    visited = [0] * (vertex_num + 1)
    # 스택에 초기값으로 시작점을 넣어줌
    stack = [start]

    # 갈 수 있는 점들이 있는 한 반복
    while stack:
        # 안 와본 점
        v_in = stack.pop()

        # 왔다고 표시
        if not visited[v_in]:
            visited[v_in] = 1

            # 인접 정점이 존재하고, 안 가본 점들 있으면 스택에 추가
            for v_out in range(1, vertex_num + 1):
                if matrix[v_in][v_out] and not visited[v_out]:
                    # NOTE: 이러면 맨 마지막 점부터 탐색 재개
                    stack.append(v_out)

                    # NOTE: 여기서부터 내용 추가
                    # 만약 해당 점이 도착점이라면 경로가 있는 거임
                    if v_out == goal:
                        return True
    
    return False


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj_matrix = input_matrix(V, E)

    S, G = map(int, input().split())
    result = dfs_path_check(adj_matrix, S, G)

    print("#{} {}".format(test_case, int(result)))
