from os import rename
from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    grid = [[0] * 10 for _ in range(10)]
    overlap = 0
    area_num = int(input())

    for _ in range(area_num):
        r1, c1, r2, c2, color = map(int, input().split())

        # 좌상단부터 우하단까지 
        for row in range(r1, r2 + 1):
            for col in range(c1, c2 + 1):
                # 같은 색이 아니거나 이미 겹친 게 아닌 경우, 색 칠하기
                if grid[row][col] != color and grid[row][col] != 3:
                    grid[row][col] += color            
                    # 겹치는 경우 겹침 횟수 증가
                    if grid[row][col] == 3:
                        overlap += 1
    
    print("#{} {}".format(test_case, overlap))