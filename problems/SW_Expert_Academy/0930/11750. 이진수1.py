from pathlib import Path
import sys


parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')

    N, hex_num = input().split()
    for hex_digit in hex_num:
        if '0' <= hex_digit <= '9':
            num = int(hex_digit)
        else:
            num = ord(hex_digit) - ord('A') + 10
        
        for i in range(3, -1, -1):
            print((num & (1 << i)) >> i, end='')
    print()
