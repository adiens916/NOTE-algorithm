def quick_sort(arr: list[int], start: int, end: int) -> None:
    # XXX: 재귀인데, 끝나는 조건이 없었음.
    # 끝나는 조건이 1개이거나, 0개인 경우도 있음.
    if start == end or start > end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # XXX: left와 right가 범위를 벗어날 수 있으니, 범위 제한 필요
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        # XXX: 범위가 동적으로 변하므로, 0과 len(arr) 대신에 start와 end가 범위임.
        # XXX: left는 end까지 검사 필요. right는 start 다음 (pivot)까지
        while start < right and arr[right] >= arr[pivot]:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            # right가 멈춘 곳이 작은 곳이므로, 피벗이랑 작은 거랑 바꿔야 함.
            arr[pivot], arr[right] = arr[right], arr[pivot]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
