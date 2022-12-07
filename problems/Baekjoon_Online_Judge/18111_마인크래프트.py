import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


def main():
    N, M, B = map(int, input().split())
    lands = [list(map(int, input().split())) for _ in range(N)]
    work_time, height = brute_force_for_min_work_time(lands, B)
    print(work_time, height)


def brute_force_for_min_work_time(lands, B):
    MAX_HEIGHT = 256

    work_times = [0] * (MAX_HEIGHT + 1)
    for height in range(MAX_HEIGHT + 1):
        work_time = dig_then_put_for_height_with_blocks(lands, height, B)
        work_times[height] = work_time

    min_work_time = min(work_times)
    heights = []
    for height in range(MAX_HEIGHT + 1):
        if min_work_time == work_times[height]:
            heights.append(height)

    return min_work_time, heights[-1]


def dig_then_put_for_height_with_blocks(lands, flat, B) -> int:
    # NOTE: MAX 값을 잘못 설정하니까 틀렸었음.
    MAX_WORK_TIME = 500 * 500 * 256 * 2
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
