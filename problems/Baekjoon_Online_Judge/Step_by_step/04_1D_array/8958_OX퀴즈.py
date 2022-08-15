import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    ox_string = input()
    score = 0
    o_num = 0

    for result in ox_string:
        if result == 'O':
            # 연속된 O 개수 1 증가
            o_num += 1
            # 해당 문제의 점수를 총합에 추가
            score += o_num
        elif result == 'X':
            # 불연속이면 0으로 초기화
            o_num = 0
    
    print(score)
