import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


def main():
    T = int(input())
    for _ in range(T):
        PS = input().strip()
        if is_VPS(PS):
            print("YES")
        else:
            print("NO")


def is_VPS(PS: str) -> bool:
    stack = []

    for P in PS:
        stack.append(P)
        if can_pair(stack):
            stack.pop()
            stack.pop()
        if has_not_paired(stack):
            return False

    return is_empty(stack)


def can_pair(stack: list[str]) -> bool:
    if len(stack) >= 2:
        if stack[-2] == "(" and stack[-1] == ")":
            return True
    return False


def has_not_paired(stack: list[str]) -> bool:
    return len(stack) > 0 and stack[-1] == ")"


def is_empty(stack: list[str]):
    return len(stack) == 0


main()
