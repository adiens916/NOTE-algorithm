from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")


T = int(input())
for test_case in range(1, T + 1):
    print("#{}".format(test_case), end=" ")

    arr = [input() for _ in range(5)]

    max_len = 0
    for e in arr:
        if len(e) > max_len:
            max_len = len(e)
    
    for col in range(max_len):
        for row in range(len(arr)):
            try:
                print(arr[row][col], end="")
            except IndexError:
                continue
    print()