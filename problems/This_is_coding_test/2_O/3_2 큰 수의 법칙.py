N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
largest = nums[0]
second = nums[1]

rep_count = M // (K + 1)
remains = M % (K + 1)

answer = rep_count * (largest * K + second) + (largest * remains)
print(answer)

"""
5 8 3
2 4 5 4 6
"""  # 46
