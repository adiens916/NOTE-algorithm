def binary_search_by_iteration(
    arr: list[int], target: int, start: int, end: int
) -> int | None:
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid

    return None


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search_by_iteration(arr, 15, 0, len(arr) - 1))
print(binary_search_by_iteration(arr, 4, 0, len(arr) - 1))
