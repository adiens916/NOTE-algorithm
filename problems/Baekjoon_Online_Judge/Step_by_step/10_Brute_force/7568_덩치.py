"""
몸무게가 크고, 키도 큰 경우,
몸무게와 키의 *합*도 크다.
"""

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


def main():
    N = int(input())
    body_sizes = []
    for i in range(N):
        weight, height = map(int, input().split())
        body_sizes.append((weight, height, i))

    # 몸무게 + 키 합으로 정렬
    body_sizes.sort(key=lambda x: sum_weight_height(x), reverse=True)

    body_ranks = [0] * N
    top = body_sizes[0][2]
    current_body_rank = 1
    body_ranks[top] = current_body_rank
    # print(body_ranks)

    duplicate_count = 0
    for i in range(1, N):
        prev_weight, prev_height, _ = body_sizes[i - 1]
        cur_weight, cur_height, k = body_sizes[i]

        # 몸무게랑 키 둘 다 같은 경우
        if cur_weight == prev_weight and cur_height == prev_height:
            body_ranks[k] = current_body_rank
        # 몸무게랑 키 둘 다 작은 경우
        elif cur_weight <= prev_weight and cur_height <= prev_height:
            current_body_rank += 1
            # 기존 중복 등수 전부 누적
            current_body_rank += duplicate_count
            duplicate_count = 0
            body_ranks[k] = current_body_rank
        # 몸무게만 작거나, 키만 작은 경우
        else:
            duplicate_count += 1
            body_ranks[k] = current_body_rank

    print(*body_ranks)


def sum_weight_height(x):
    return x[0] + x[1]


main()
