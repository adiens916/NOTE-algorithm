N = int(input())
nums = list(map(int, input().split()))
nums.sort()

# XXX: 결국 거리 합을 최소로 만드는 곳은, 정렬 했을 때 중앙에 있는 곳임.
median = nums[(N - 1) // 2]

print(median)

"""
4
5 1 7 9
"""  # 5
"""
4
1 2 9 10
"""  # 2
"""
3
1 9 10
"""  # 9
