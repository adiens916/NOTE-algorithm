
from pathlib import Path
import os
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
    pos = 0
    charge_count = 0

    while pos + reach < destination:
        if pos + reach < stations[last]:
            charge_count = 0
            break
        elif pos + reach == stations[last]:
            pos += reach
            charge_count += 1
            last += 1
        else:
            while last < station_num and pos + reach >= stations[last]:
                last += 1
            pos = stations[last - 1]
            charge_count += 1
        
        if last >= station_num:
            last = station_num - 1

    print("#{} {}".format(test_case, charge_count))