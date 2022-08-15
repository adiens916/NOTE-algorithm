from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def dfs(k, cur_sum, left_sum):
    global min_diff
    # 가지치기: 최솟값보다 큼
    if cur_sum - B > min_diff:
        return
    # 가지치기: 나머지 더해도 안 됨
    if cur_sum + left_sum < B:
        return

    # 종료 조건: 선반보다 커지거나, 끝에 도달
    if cur_sum > B or k == -1:
        min_diff = min(min_diff, cur_sum - B)
        return
    # 뽑고, 안 뽑고 
    # 뒤에서부터 선택하면 가지를 줄일 수 있음 & N 인자 불필요.
    dfs(k - 1, cur_sum + arr[k], left_sum - arr[k])
    dfs(k - 1, cur_sum, left_sum - arr[k])


T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    S = sum(arr)
    min_diff = 987654321
    dfs(N - 1, 0, S)

    print(f'#{test_case} {min_diff}')
