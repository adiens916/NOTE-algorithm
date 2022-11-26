import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


def main():
    K, N = map(int, input().split())
    cables = [int(input()) for _ in range(K)]
    result = find_max_length_when_N(cables, N)
    print(result)


def find_max_length_when_N(cables: list[int], N: int) -> int:
    max_length = 0
    min_range = 1
    max_range = min(cables)

    # FIX: 같은 것도 포함해야 함
    while min_range <= max_range:
        mid = (min_range + max_range) // 2
        cut_count = count_cables_cut_by_length(cables, mid)

        if cut_count < N:
            max_range = mid - 1
        else:
            min_range = mid + 1
            if max_length < mid:
                max_length = mid

    return max_length


def count_cables_cut_by_length(cables: list[int], cut_len: int) -> int:
    count = 0
    for cable in cables:
        count += cable // cut_len
    return count


main()
