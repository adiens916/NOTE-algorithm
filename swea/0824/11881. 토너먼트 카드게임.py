from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def rock_scissor_paper(a_card, a_idx, b_card, b_idx):
    if a_card == b_card:
        return a_card, a_idx
    elif a_card - b_card == 1 or b_card - a_card == 2:
        return a_card, a_idx
    elif b_card - a_card == 1 or a_card - b_card == 2:
        return b_card, b_idx


def divide_conquer(arr, start, end):
    if start == end:
        return arr[start], start
    else:
        a, a_idx = divide_conquer(arr, start, (start + end) // 2)
        b, b_idx = divide_conquer(arr, (start + end) // 2 + 1, end)
        w, w_idx = rock_scissor_paper(a, a_idx, b, b_idx)
        return w, w_idx


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    _, winner = divide_conquer(arr, 1, N)
    print("#{} {}".format(test_case, winner))
