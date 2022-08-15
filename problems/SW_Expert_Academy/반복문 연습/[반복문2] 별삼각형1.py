
from pathlib import Path
import os
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case}")

    length, shape = map(int, input().split())
    if shape == 1:
        for num in range(1, length + 1):
            print("*" * num)
    elif shape == 2:
        for num in range(length, 0, -1):
            print("*" * num)
    elif shape == 3:
        for num in range(1, length + 1):
            print(" " * (length - num), end="")
            print("*" * (num * 2 - 1), end="")
            print(" " * (length - num))
    else:
        pass


"""
출력

#1
*
**
***
#2
***
**
*
#3
  *
 ***
*****
"""