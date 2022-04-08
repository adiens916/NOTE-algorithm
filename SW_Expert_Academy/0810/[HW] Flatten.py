"""
일단 전체 합으로는 안 됨.

-> 개별로?
최대, 최소 계속 갱신하면서 가운데로 수렴되도록?


"""


from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    
    # 카운팅 정렬 응용
    height_counts = [0] * 101
    for n in range(len(boxes)):
        height_counts[boxes[n]] += 1
    
    max_height = 100
    min_height = 1
    while dump > 0:
        # 현재 최대 높이랑 최소 높이 찾기
        while height_counts[max_height] == 0:
            max_height -= 1
        while height_counts[min_height] == 0:
            min_height += 1
        
        # 최대-최소 차이가 1 이내인 경우
        # -> 평탄화 됐으므로 종료
        if max_height - min_height <= 1:
            break

        # 블럭을 덤프하면, 최대에서 하나를 빼 최소로 옮긴다.
        # -> 최대와 최소에 해당하는 블록들이 하나씩 감소한다.
        height_counts[max_height] -= 1
        height_counts[min_height] -= 1
        
        # 반면 최대에서 하나를 뺐으니, 그 높이에 해당하는 블록 수는 증가
        # 마찬가지로 최소에 하나를 더했으니, 그 높이의 블록 수는 증가
        height_counts[max_height - 1] += 1
        height_counts[min_height + 1] += 1
        dump -= 1
    
    # 마지막 덤프 때 한 개 남았던 블록이 메꿔져서 
    # 최소 높이가 39에서 40으로 바뀌는 경우 있음 (6번 케이스)
    # -> 마지막으로 한 번 더 최대 높이 & 최소 높이 갱신
    while height_counts[max_height] == 0:
        max_height -= 1
    while height_counts[min_height] == 0:
        min_height += 1
        
    print("#{} {}".format(test_case, max_height - min_height))
    