import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


def main():
    N = int(input())
    stack_sequence = [int(input()) for _ in range(N)]
    result = trace_stack_sequence(stack_sequence)
    print(*result, sep="\n")


def trace_stack_sequence(stack_sequence: list[int]) -> list[str]:
    N = len(stack_sequence)
    idx = 0
    stack = []
    answer = []

    for num in range(1, N + 1):
        stack.append(num)
        answer.append("+")

        while stack and stack[-1] == stack_sequence[idx]:
            stack.pop()
            answer.append("-")
            idx += 1

    if any(stack):
        answer = ["NO"]
    return answer


main()
