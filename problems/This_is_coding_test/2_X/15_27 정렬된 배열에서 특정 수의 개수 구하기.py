def binary_search_left(arr, x) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1

    # XXX: 현재 배열에 있는 것보다 더 큰 숫자인 경우, left는 배열 범위를 벗어나게 됨
    # => 범위 체크 필요. 이게 1회차 때보다 더 효율적임. (한 번만 판단하니까)
    if left < len(arr) and arr[left] == x:
        return left
    else:
        return -1


def binary_search_right(arr, x) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    if 0 <= right and arr[right] == x:
        return right
    else:
        return -1


N, x = map(int, input().split())
arr = list(map(int, input().split()))

start = binary_search_left(arr, x)
end = binary_search_right(arr, x)

if start == -1:
    print(-1)
else:
    print(end - start + 1)

"""
7 2
1 1 2 2 2 2 3 
"""  # 4
"""
7 4
1 1 2 2 2 2 3 
"""  # -1
