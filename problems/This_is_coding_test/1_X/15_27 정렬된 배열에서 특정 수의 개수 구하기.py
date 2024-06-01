N, target = map(int, input().split())
nums = list(map(int, input().split()))


# 왼쪽 target 구하기
def bisect_left():
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:  # nums[mid] == target
            # 맨 첫 번째면 0 반환
            if mid - 1 < 0:
                return 0
            # 왼쪽이 원하는 숫자가 아니면 시작 지점임
            if nums[mid - 1] != target:
                return mid
            # 왼쪽도 숫자가 같으면, 좀 더 왼쪽으로 가야 함
            else:
                end = mid - 1
    return -1


# 오른쪽 target 구하기
def bisect_right():
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:  # nums[mid] == target
            # 맨 끝 이후로 없으면, 끝 지점 반환
            if N - 1 < mid + 1:
                return N - 1
            # 오른쪽이 원하는 숫자가 아니면 목표의 끝 지점임
            if nums[mid + 1] != target:
                return mid
            # 오른쪽도 숫자가 같으면, 좀 더 오른쪽으로 가야 함
            else:
                start = mid + 1
    return -1


left = bisect_left()
right = bisect_right()

if left == -1:
    print(-1)
else:
    print(right - left + 1)

"""
7 2
1 1 2 2 2 2 3
"""  # 4
"""
7 4
1 1 2 2 2 2 3
"""  # -1
