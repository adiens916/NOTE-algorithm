def quick_sort(arr: list[int], start: int, end: int) -> None:
    # X: 시작과 끝이 '같음' = 1개만 있음 = 정렬 불필요
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    # XXX: 왼쪽과 오른쪽이 '같음' = 2개만 있음 = 비교 후 정렬 필요
    while left <= right:
        # X: 맨 끝 요소'까지' 체크
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        # X: '같은' 것도 넘어가도 됨
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[start], arr[right] = arr[right], arr[start]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
