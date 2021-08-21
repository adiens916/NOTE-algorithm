from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    print("#{}".format(test_case), end=" ")

    # 노선 정보 입력
    route_num = int(input())
    routes = [0] * route_num
    for i in range(route_num):
        routes[i] = tuple(map(int, input().split()))
    
    # 정류장 정보 입력
    station_num = int(input())
    for i in range(station_num):
        station = int(input())
        avaliable = 0

        # 각 정류장별로 노선 어느 범위에 걸쳐있는지 확인
        for route in routes:
            if route[0] <= station <= route[1]:
                avaliable += 1
        
        # 가능한 노선 개수 출력
        print(avaliable, end=" ")
    print()
