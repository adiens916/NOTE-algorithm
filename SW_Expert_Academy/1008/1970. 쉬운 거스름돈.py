from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


coin_types = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    coin_count = [0] * len(coin_types)

    for i in range(len(coin_types)):
        coin_count[i] = N // coin_types[i]
        N %= coin_types[i]
    
    print(f'#{test_case}')
    print(*coin_count, sep=' ')
