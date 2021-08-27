from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def print_inorder(node):
    if node:
        print_inorder(lefts[node])
        print(values[node], end="")
        print_inorder(rights[node])


T = 10
for test_case in range(1, T + 1):
    N = int(input())
    values = [0] * (N + 1)
    lefts = [0] * (N + 1)
    rights = [0] * (N + 1)

    for _ in range(N):
        info = input().split()
        node = int(info[0])
        values[node] = info[1]
        if node * 2 <= N:
            lefts[node] = int(info[2])
        if node * 2 + 1 <= N:
            rights[node] = int(info[3])

    print("#{}".format(test_case), end=" ")
    print_inorder(1)
    print()
