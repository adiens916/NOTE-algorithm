from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
서로소 집합

FIXME: 순서가 다른 2 3 1 2 같은 경우도 고려했어야 함
=> 나중에 전체를 한 번 더 갱신
"""

def represent(x):
    while group[x] != x:
        x = group[x]
    return x


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 자기 자신을 대표 원소로 하는 서로소 집합
    group = list(range(N + 1))
    
    pairs = list(map(int, input().split()))
    for i in range(M):
        x, y = pairs[2 * i], pairs[2 * i + 1]
        
        # 무조건 앞의 작은 쪽이 대표
        if x > y:
            x, y = y, x

        # y를 x쪽에 편입
        group[represent(y)] = represent(x)
    
    # FIXME: 대표 원소 갱신
    for i in range(1, N + 1):
        group[i] = represent(i)

    # 서로소 집합의 중복을 제거한 개수를 구하고,
    # 맨 처음에 포함된 0을 제거
    pair_count = len(set(group)) - 1

    print('#{} {}'.format(test_case, pair_count))
