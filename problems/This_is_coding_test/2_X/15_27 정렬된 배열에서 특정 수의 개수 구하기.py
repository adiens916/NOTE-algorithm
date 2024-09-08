def binary_search_left(arr, x) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1

    target = right
    if arr[target] == x:
        return target
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

    target = left
    if arr[target] == x:
        return target
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
