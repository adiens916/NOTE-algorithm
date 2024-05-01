import sys
input = sys.stdin.readline

import heapq


N = int(input())
nums = [int(input()) for _ in range(N)]

# 힙 정렬 이용 (NlogN)
# 왜냐하면 정렬해서 맨 앞부터 더하다 보면, 뒤에 있는 것보다 커지기 때문.
# 따라서 항상 최소를 보장하면서 속도가 빠른 힙 정렬을 이용함.
heapq.heapify(nums)

total_comp_count = 0
# 큐에 하나만 남을 때까지 반복 (N - 1번)
while len(nums) > 1:
    # 가장 작은 수 2개 뽑음 (logN + logN)
    min_num = heapq.heappop(nums)
    next_min_num = heapq.heappop(nums)

    # 비교 횟수 구한 다음, 더하고 다시 큐에 넣기
    comp_count = min_num + next_min_num
    total_comp_count += comp_count
    heapq.heappush(nums, comp_count)

print(total_comp_count)

"""
3
10
20
40
"""  # 100
"""
5
1
1
2
2
2
"""  # 18
"""
1 1 2 2 2

(2)
2 2 2 2  

(2 + 4)
4 2 2  

(A) (2 + 4 + 6)
6 2

(2 + 4 + 6 + 8) = 20
8

(B) (2 + 4 + 4)
4 4

(2 + 4 + 4 + 8) = 18
8
"""
