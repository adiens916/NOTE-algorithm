from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def permut(k, prev, cur_sum):
    global min_sum

    # 백트래킹
    if cur_sum > min_sum:
        return

    # 종료 조건: N개 전부 골랐을 때
    if N == k:
        # 최솟값 갱신
        min_sum = min(cur_sum + arr[prev][0], min_sum)
    else:
        # 방문 체크를 이용한 순열
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                # 이전 지점과, 이전 지점 ~ 현재 지점까지의 비용 추가
                permut(k + 1, i, cur_sum + arr[prev][i])
                visited[i] = False


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 123456789

    # 방문 배열. 첫 번째는 무조건 방문한 채로 시작.
    visited = [False] * N
    visited[0] = True
    permut(1, 0, 0)

    print('#{} {}'.format(test_case, min_sum))
