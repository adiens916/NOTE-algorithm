from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def count_binary_search(left, right, target):
    count = 0
    
    while True:
        center = (left + right) // 2
        count += 1

        if center == target:
            break
        elif center < target:
            left = center
        elif center > target:
            right = center
        else:
            pass
    
    return count


T = int(input())
for test_case in range(1, T + 1):
    book, page_a, page_b = map(int, input().split())
    count_a = count_binary_search(1, book, page_a)
    count_b = count_binary_search(1, book, page_b)
    
    winner = "A" if count_a < count_b else "B" if count_a > count_b else "0"
    print("#{} {}".format(test_case, winner))