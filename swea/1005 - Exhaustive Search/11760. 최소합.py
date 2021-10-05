from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def dp(x, y):
    # 끝에 도달하면 종료
    if x == N - 1 and y == N - 1:
        return arr[y][x]

    # 범위 체크: 
    if 0 <= x < N and 0 <= y < N:
        # 처음 방문하는 곳인 경우,
        if not memo[y][x]:
            # 아래쪽과 오른쪽 중 더 작은 쪽을 찾아, 현재 지점에 저장
            # => 항상 최소가 되는 경로를 찾을 수 있음
            memo[y][x] = arr[y][x] + min(dp(x, y + 1), dp(x + 1, y))
        # 이미 방문한 경우엔, 그대로 반환
        return memo[y][x]
    else:    
        # 범위 벗어난 경우, 다른 쪽을 선택하게끔 최댓값을 리턴
        return max_sum


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    memo = [[0] * N for _ in range(N)]

    max_sum = 2 * N * 10
    dp(0, 0)

    print('#{} {}'.format(test_case, memo[0][0]))


"""
def dfs(x, y, cur_sum):
    global min_sum
    # 백트래킹: 최소보다 큰 경로는 X
    if cur_sum > min_sum:
        return
    # 범위 체크
    if not (0 <= x < N and 0 <= y < N):
        return

    # 범위 안이면 해당 지점의 값 더함
    cur_sum += arr[x][y]
    # 종료 조건: 오른쪽 아래에 도달
    if x == N - 1 and y == N - 1:
        min_sum = min(cur_sum, min_sum)
        return
    else:
        dfs(x, y + 1, cur_sum)
        dfs(x + 1, y, cur_sum)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 2 * N * 10
    dfs(x=0, y=0, cur_sum=0)

    print('#{} {}'.format(test_case, min_sum))
"""
