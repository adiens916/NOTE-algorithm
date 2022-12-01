import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    cut_height = binary_search_for_min_sum_of_cut(trees, M)
    print(cut_height)


def binary_search_for_min_sum_of_cut(trees: list[int], M: int) -> int:
    min_range = 0
    max_range = max(trees)

    max_cut_height = 0
    MAX_TREE_HEIGHT = 1000000000
    min_sum_of_cut = MAX_TREE_HEIGHT * len(trees)

    while min_range <= max_range:
        mid = (min_range + max_range) // 2
        sum_of_cut = sum([tree - mid for tree in trees if tree >= mid])

        if sum_of_cut < M:
            max_range = mid - 1
        else:
            min_range = mid + 1
            if sum_of_cut < min_sum_of_cut:
                min_sum_of_cut = sum_of_cut
                max_cut_height = mid

    return max_cut_height


main()
