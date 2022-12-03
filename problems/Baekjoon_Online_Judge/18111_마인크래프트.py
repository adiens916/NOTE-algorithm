import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


MAX_WORK_TIME = 256 * 25000 * 2


def main():
    N, M, B = map(int, input().split())
    lands = [list(map(int, input().split())) for _ in range(N)]
    work_time, height = binary_search_by_min_work_time(lands, B)
    print(work_time, height)


def binary_search_by_min_work_time(lands, B) -> tuple[int, int]:
    min_range = min((min(line) for line in lands))
    max_range = max((max(line) for line in lands))
    best_work_time = MAX_WORK_TIME
    best_height = 0

    while min_range <= max_range:
        mid = (min_range + max_range) // 2
        work_time = dig_then_put_for_height_with_blocks(lands, mid, B)

        if work_time >= best_work_time:
            max_range = mid - 1
        else:
            min_range = mid + 1
            best_work_time = work_time
            best_height = mid

    return best_work_time, best_height


def dig_then_put_for_height_with_blocks(lands, flat, B) -> int:
    work_time = 0

    for line in lands:
        for block in line:
            if block >= flat:
                diff = block - flat
                # dig
                B += diff
                work_time += diff * 2

            elif block < flat:
                diff = flat - block
                # put
                B -= diff
                work_time += diff

    if B < 0:
        return MAX_WORK_TIME
    else:
        return work_time


main()
