from pathlib import Path
import sys


parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    daily_fee, monthly_fee, quarterly_fee, yearly_fee = \
        map(int, input().split())
    schedule = list(map(int, input().split()))
    min_prefix_sum = [0] * 13

    for month in range(1, 13):
        # 이전까지의 최소 합을 그대로 이어받음
        min_prefix_sum[month] = min_prefix_sum[month - 1]

        # 1일짜리 비용
        daily_cost = schedule[month - 1] * daily_fee

        # 1일짜리 vs. 1개월짜리 -> 더 작은 쪽을 저장
        min_prefix_sum[month] += min(daily_cost, monthly_fee)
        
        # 3개월짜리는 (3개월 이전 합 + 이번 3개월치 비용)
        # 마찬가지로 더 작은 쪽을 저장
        if month >= 3: 
            prev_quarter_sum = min_prefix_sum[month - 3]
            quarter_sum = prev_quarter_sum + quarterly_fee
            min_prefix_sum[month] = min(min_prefix_sum[month], quarter_sum)

    # 여태까지의 최소 합과 1년짜리 비교    
    min_prefix_sum[12] = min(min_prefix_sum[12], yearly_fee)

    print('#{} {}'.format(test_case, min_prefix_sum[12]))
