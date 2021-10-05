from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

"""
큰 트럭이, 가능한 큰 화물을 싣고 가면 됨 => 그리디
"""

T = int(input())
for test_case in range(1, T + 1):
    cargo_num, truck_num = map(int, input().split())
    # 큰 게 맨 앞에 오도록 정렬
    cargos = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)

    weight_sum = 0
    cargo_index = 0
    # 각각의 트럭들에 대해
    for truck in trucks:
        # 화물이 트럭 용량보다 크면 다음 화물로 넘어감
        while cargo_index < cargo_num and cargos[cargo_index] > truck:
            cargo_index += 1
        # 모든 화물을 살펴본 경우엔 끝냄
        if cargo_index == cargo_num:
            break
        
        # 트럭 용량보다 작으므로 해당 화물을 싣고 감
        weight_sum += cargos[cargo_index]
        cargo_index += 1
    
    print('#{} {}'.format(test_case, weight_sum))
