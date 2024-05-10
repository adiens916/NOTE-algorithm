# Longest Increasing Subsequence (LIS) 문제

n = int(input())
nums = list(map(int, input().split()))

nums.reverse()
max_lengths = [1] * n

for anchor in range(n):
    for prev in range(anchor):
        if nums[prev] < nums[anchor]:
            # XXX: 그냥 이전 값 + 1로만 갱신하는 경우,
            # 중간에 작은 숫자가 나와버리면 더 작은 숫자로 갱신되어버림
            # => 항상 최댓값으로 갱신되도록, max 함수로 비교하기
            max_lengths[anchor] = max(max_lengths[anchor], max_lengths[prev] + 1)

# XXX: 최댓값이 중간에 나올 수도 있으므로, 끝 지점을 출력하면 안됨
print(n - max(max_lengths))

"""
7
15 11 4 8 5 2 4
"""  # 2
"""
11
100 7 6 5 4 3 10 9 8 2 1
"""  # 3 => 뒤쪽의 10 9 8을 빼는 게 이득
"""
8
100 4 3 10 9 8 2 1
"""  # 2 => 앞쪽의 4 3을 빼는 게 이득
