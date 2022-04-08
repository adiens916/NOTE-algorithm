from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def dfs_by_bit(k, bit, cur_success):
    global max_success

    # 가지치기
    if cur_success <= max_success:
        return
    
    # 종료조건
    if N == k:
        max_success = cur_success

    for i in range(N):
        # 방문체크
        if not (bit & 1 << i):
            # 현 지점 방문 체크 & 확률을 곱함
            dfs_by_bit(k + 1, bit | 1 << i, cur_success * (arr[k][i] / 100))


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_success = 0.0

    dfs_by_bit(0, 0, 100)

    print(f'#{test_case} {max_success:.6f}')
