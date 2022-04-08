from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def dfs(start, cur_exchange):
    global min_exchange

    # 가지치기: 최솟값보다 크면 중지
    if cur_exchange > min_exchange:
        return

    # 종료조건: 마지막 넘어갈 시 최솟값 갱신
    if start >= station_num - 1:
        min_exchange = min(min_exchange, cur_exchange)

    else:
        energy = stations[start]
        # 에너지를 1씩 줄이며 갈 수 있는 모든 경우를 체크
        for reach in range(energy, 0, -1):
            dfs(start + reach, cur_exchange + 1)


T = int(input())
for test_case in range(1, T + 1):
    station_num, *stations = list(map(int, input().split()))
    # 최대 100개의 정류장이므로, 최대 100번만 교환 가능
    min_exchange = 100
    # 처음 교환 횟수는 반영하지 않으므로, -1
    dfs(start=0, cur_exchange=-1)

    print('#{} {}'.format(test_case, min_exchange))
