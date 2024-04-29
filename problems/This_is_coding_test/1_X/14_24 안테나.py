N = int(input())
nums = list(map(int, input().split()))
nums.sort()

avg = sum(nums) / len(nums)

median = 100001
for num in nums:
    if abs(num - avg) < abs(median - avg):
        median = num
    else:
        break

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
