"""
퀵 정렬
"""

def partition(arr, start, end):
    middle = (end + start) // 2
    pivot = arr[middle][1]
    arr[middle], arr[start] = arr[start], arr[middle]
    
    left = start
    right = end

    while True:
        while left <= end and arr[left][1] <= pivot:
            left += 1
        while start <= right and arr[right][1] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[start], arr[right] = arr[right], arr[start]
            return right - 1, left


def quicksort(arr, start, end):
    if start < end:
        new_end, new_start = partition(arr, start, end)
        quicksort(arr, start, new_end)
        quicksort(arr, new_start, end)


N = int(input())
arr = []
for _ in range(N):
    name, score = input().split()
    arr.append((name, int(score)))

quicksort(arr, 0, N - 1)
print(*[name for name, score in arr])


"""
2
홍길동 95
이순신 77
"""
