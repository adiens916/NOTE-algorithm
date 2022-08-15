import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


C = int(input())
for _ in range(C):
    N, *scores = list(map(int, input().split()))
    # 0. 점수들 범위가 더 작으므로, 점수들 배열이 더 찾기 쉬움.
    score_arr = [0] * 101
    score_sum = 0

    # 1. 평균 구하기 & 계수 배열에 넣기
    for score in scores:
        score_sum += score
        score_arr[score] += 1
    avg = score_sum / N

    # 2. 평균 넘는 학생들 찾기
    avg_ceil = int(avg * 10 // 10) + 1
    count_above_avg = 0
    for i in range(avg_ceil, 101):
        count_above_avg += score_arr[i]
    
    # 3. 비율 구하기
    ratio = 100 * count_above_avg / N

    # 4. 셋째 자리까지 출력
    print(f'{ratio:.3f}%')
