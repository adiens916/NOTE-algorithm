"""
정렬할 필요없이,
(떨어질 수 있는 높이 - 밑에 겹치는 블럭 개수)로
구할 수 있었음...

처음에는 밑에 블럭이 없을 때 높이로 접근
즉, 최대한 단순하게 접근하고
거기에 조건을 하나씩 덧붙이는 식으로
"""

from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem.split()[0]

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    block_num = int(input())
    blocks = list(map(int, input().split()))
    max_height = 0

    for base in range(block_num):
        height = block_num - base - 1
        for down in range(base + 1, block_num):
            if blocks[down] >= blocks[base]:
                height -= 1
        
        max_height = height if height > max_height else max_height

    print(f"#{test_case} {max_height}")