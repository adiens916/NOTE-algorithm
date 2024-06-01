def quick_sort(arr: list[tuple[str, int]], start: int, end: int) -> None:
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left][1] <= arr[pivot][1]:
            left += 1
        while right > start and arr[right][1] >= arr[pivot][1]:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[pivot], arr[right] = arr[right], arr[pivot]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


N = int(input())
students = []
for _ in range(N):
    name, score = input().split()
    students.append((name, int(score)))

quick_sort(students, 0, N - 1)
names = [name for name, score in students]
print(*names)

"""
2
홍길동 95
이순신 77
"""
