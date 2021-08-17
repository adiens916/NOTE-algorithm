from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def find_pattern(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                break
        else:
            return i
    
    return -1



T = int(input())
for test_case in range(1, T + 1):
    pattern = input().rstrip()
    text = input().rstrip()
    position = find_pattern(text, pattern)

    result = 1 if position > -1 else 0
    print("#{} {}".format(test_case, position))
