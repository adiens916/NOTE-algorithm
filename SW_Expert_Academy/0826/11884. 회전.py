from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


from collections import deque


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    Q = deque([int(n) for n in input().split()])

    for _ in range(M):
        # Q.append(Q.popleft())
        Q.rotate(-1)

    print("#{} {}".format(test_case, Q[0]))
