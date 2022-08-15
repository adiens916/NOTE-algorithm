"""
기존에 더해놓은 값을 이용하는 문제
"""

from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


start_num = ord('A')
cycle = ord('Z') - ord('A') + 1

T = int(input())
for test_case in range(1, T + 1):
    print("#{}".format(test_case))

    N = int(input())
    for row in range(N):
        print(" " * (N - row - 1), end='')

        for col in range(row + 1):
            if col == 0:
                offset = row % cycle
                prev = offset
            else:
                offset = (prev + N - col) % cycle
                prev = offset
            print(chr(offset + start_num), end=" ")

        print()
    
