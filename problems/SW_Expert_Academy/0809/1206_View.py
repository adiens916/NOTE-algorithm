from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


for N in range(10):
    print(f"#{N + 1}", end=" ")
    view_available = 0

    building_num = int(input())
    buildings = list(map(int, input().split()))
    for i in range(2, building_num - 2):
        # 주위 2칸 이내 중 제일 큰 빌딩의 높이를 구한다.
        # 단, 가운데 빌딩은 제외한다.
        adjacent_highest = max(*buildings[i - 2:i], *buildings[i + 1:i + 3])
        
        # 그 빌딩 높이보다 큰 층수만 조망권이 확보된다.
        higher = buildings[i] - adjacent_highest
        if higher > 0:
            view_available += higher
    
    print(view_available)