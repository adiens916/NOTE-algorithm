def binary_search(arr: list[int], target: int, start: int, end: int) -> int:
    if start > end:
        return -1

    mid = (start + end) // 2
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return mid


arr = list(map(int, input().split()))
for _ in range(2):
    target = int(input())
    print(binary_search(arr, target, 0, len(arr) - 1))


"""
1 3 5 7 9 11 13 15 17 19
4
17
"""
