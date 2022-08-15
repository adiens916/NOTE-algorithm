from pathlib import Path
directory = Path(__file__).parent
file_name = Path(__file__).stem
input_text = f"{directory}\{file_name}_input.txt"

import sys
sys.stdin = open(input_text)
input = sys.stdin.readline

##################################################
from collections import deque


city_count, road_count, wanted_length, original_start = map(int, input().split())

# 도시 번호가 1부터 시작하므로, 총 개수는 1 더 크게 만들어야 함.
paths = [[] for _ in range(city_count + 1)]
for _ in range(road_count):
    start, destination = map(int, input().split())
    paths[start].append(destination)

lengths_to_city = [0] * (city_count + 1)
target_cities = []

# 최단 거리 찾는 것이므로 BFS
queue = deque()
queue.append(original_start)
while queue:
    start = queue.popleft()
    
    for destination in paths[start]:
        # 방문했으면 스킵
        if lengths_to_city[destination] > 0:
            continue

        if lengths_to_city[destination] < wanted_length:
            lengths_to_city[destination] = lengths_to_city[start] + 1
        
            if lengths_to_city[destination] == wanted_length:
                target_cities.append(destination)

            queue.append(destination)
            

if not target_cities:
    print(-1)
else:
    for city in sorted(target_cities):
        print(city)
