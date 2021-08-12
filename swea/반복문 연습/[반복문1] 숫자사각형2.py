
from pathlib import Path
import os
import sys

parent_dir = Path(__file__).parent
file_name = os.path.basename(__file__).split('.')[0]

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for t in range(T):
    print(f'#{t + 1}')
 
    H, W = map(int, input().split())
    for row in range(H):
        for col in range(W):
            print(row + 1 + col * H, end=' ')
        print()