from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

"""
더 이상 못 가면 개수 세기

무조건 못 가는 조건: 벽 체크
판별: 
- 방문 체크
- 서로간의 숫자 차이가 1 초과
"""



# 상 하 좌 우
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def dfs(row, col, visit_num):

    for i in range(4):
        y = row + dy[i]
        x = col + dx[i]
        if 0 <= y < N and 0 <= x < N:
            if arr[row][col] + 1 == arr[y][x]:
                dfs(y, x, visit_num + 1)
            
        


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_start = 0
    max_room = 0
    visited = [[False] * N for _ in range(N)]



    print(f'{test_case}')