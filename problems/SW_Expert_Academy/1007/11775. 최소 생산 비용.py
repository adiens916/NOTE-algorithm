from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
100 010 001
1{1}0 10{1}
11{1} 1{1}1
"""

def dfs_by_bit(n, k, bit, cur_cost):
    global min_cost

    # 가지치기: 최솟값보다 커지면 중지
    if cur_cost > min_cost:
        return
    
    # 종료조건
    if n == k:
        min_cost = min(min_cost, cur_cost)

    for i in range(n):
        # 방문체크
        if bit & 1 << i:
            continue
        
        # 현 지점 방문 체크 & 비용을 추가
        dfs_by_bit(n, k + 1, bit | 1 << i, cur_cost + arr[k][i])


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_cost = N * N * 100

    dfs_by_bit(N, k=0, bit=0, cur_cost=0)

    print(f'#{test_case} {min_cost}')
