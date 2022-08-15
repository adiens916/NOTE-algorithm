from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


from collections import deque


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    dup_set = set()
    min_count = 1000000

    start = [[M, 0]]
    queue = deque(start)
    while queue:
        num, count = queue.popleft()

        # 범위 체크
        if not (0 < num <= 1000000):
            continue

        # 중복 체크
        if num in dup_set:
            continue
        dup_set.add(num)

        # 종료 조건
        if num == N:
            min_count = count
            break

        # 연산 가능 경우 거꾸로: -1, +1, //2, +10
        count += 1
        if num % 2 == 0:
            queue.append((num // 2, count))
        queue.append((num - 1, count))
        queue.append((num + 1, count))
        queue.append((num + 10, count))    
    
    print('#{} {}'.format(test_case, min_count))
