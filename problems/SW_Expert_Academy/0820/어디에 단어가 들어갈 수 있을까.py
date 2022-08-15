from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range(N):
        seq = 0
        for j in range(N):
            if arr[i][j] == 1:
                seq += 1
            else:
                if seq == K:
                    count += 1
                seq = 0
        if seq == K:
            count += 1
        
        seq = 0
        for j in range(N):
            if arr[j][i] == 1:
                seq += 1
            else:
                if seq == K:
                    count += 1
                seq = 0
        if seq == K:
            count += 1
    
    print("#{} {}".format(test_case, count))
