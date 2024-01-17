import random


def quick_sort(arr: list[int], start: int, end: int) -> None:
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:  # XXX: 엇갈리기 전까지 계속 교환
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left < right:  # XXX: 서로 같아질 일은 절대로 없음. 부등호로 충분함.
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[pivot], arr[right] = arr[right], arr[pivot]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

quick_sort(arr, 0, len(arr) - 1)
print(arr)
