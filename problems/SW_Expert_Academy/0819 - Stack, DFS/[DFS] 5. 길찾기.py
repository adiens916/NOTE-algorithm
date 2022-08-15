from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
# input = sys.stdin.readline


def dfs_path_check(matrix):
    start = 0
    goal = 99

    visited = [0] * 100
    stack = [start]

    while stack:
        v_in = stack.pop()
        if not visited[v_in]:
            visited[v_in] = 1
            
            for i in range(2):
                v_out = matrix[i][v_in]
                if v_out and not visited[v_out]:
                    stack.append(v_out)

                    if v_out == goal:
                        return True
    
    return False


T = 10
for test_case in range(1, T + 1):
    test_case, path_num = map(int, input().split())
    edges = list(map(int, input().split()))

    adj_arr = [[0] * 100, [0] * 100]
    for n in range(path_num):
        v_in, v_out = edges[2*n], edges[2*n + 1]
        if not adj_arr[0][v_in]:
            adj_arr[0][v_in] = v_out
        else:
            adj_arr[1][v_in] = v_out
    
    result = dfs_path_check(adj_arr)
    print("#{} {}".format(test_case, int(result)))
