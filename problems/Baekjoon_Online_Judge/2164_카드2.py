from collections import deque
import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


def main():
    N = int(input())
    print(pick_from_queue(N))


def pick_from_queue(N: int):
    nums = [i for i in range(1, N + 1)]
    queue = deque(nums)
    pick = -1

    while queue:
        pick = queue.popleft()
        if queue:
            queue.append(queue.popleft())

    return pick


def pick_from_queue_by_index(N: int, gap: int):
    """느림"""
    nums = [i for i in range(1, N + 1)]
    index = 0
    pick = -1

    while nums:
        pick = nums.pop(index)

        if len(nums) > 0:
            index = (index + gap - 1) % len(nums)

    return pick


main()
