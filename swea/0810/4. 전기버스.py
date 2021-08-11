"""
방법
1. 거리로, 앞에서부터
2. 정류장 인덱스로, 뒤에서부터
(더 많이 가는 경우 고려해서)
"""

from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    reach, destination, station_num = list(map(int, input().split()))
    stations = list(map(int, input().split()))
    last = 0
    current = 0
    charge_count = 0

    # 현재 위치에서 갔는데 도착지에 못 가면 반복
    while current + reach < destination:
        # 갈 수 있는 만큼 갔는데 다음 정류장까지 못 가면 더 이상 못 감
        if current + reach < stations[last]:
            charge_count = 0
            break
        # 딱 정류장까지 맞게 가면 거기서 충전
        elif current + reach == stations[last]:
            current += reach
            charge_count += 1
            last += 1
        # 현재 지정된 정류장보다 많이 갔으면
        else:
            # 정류장이 더 멀어질 때까지, 다음 정류장과 비교
            while last < station_num and current + reach >= stations[last]:
                last += 1
            # 정류장이 더 멀어진 경우, 바로 이전 정류장까지 가는 걸로 변경
            current = stations[last - 1]
            charge_count += 1
        
        # 마지막 정류장보다 멀리 간 경우, 그냥 마지막 정류장으로 갱신
        if last >= station_num:
            last = station_num - 1

    print("#{} {}".format(test_case, charge_count))