N = int(input())
nums = list(map(int, input().split()))


def bisect_fixed_point(N: int, nums: list[int]) -> int:
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        # 인덱스보다 값이 큰 경우
        # 이 경우, 인덱스 + 1 지점은, 아까 값보다 무조건 큰 값이 나옴.
        # 즉, 우측으로 가면 인덱스의 증가율보다, 값의 증가율이 더 크므로, 고정점은 절대 없음.
        if mid < nums[mid]:
            # 더 작은 쪽 찾기
            right = mid - 1
        # 인덱스보다 값이 작은 경우
        elif mid > nums[mid]:
            # 더 큰 쪽 찾기
            left = mid + 1
        else:  # mid == nums[mid]
            return mid

    return -1


fixed_point = bisect_fixed_point(N, nums)
print(fixed_point)

"""
5
-15 -6 1 3 7
"""  # 3
"""
7
-15 -4 2 8 9 13 15
"""  # 2
"""
7
-15 -4 3 8 9 13 15
"""  # -1
