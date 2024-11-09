def selective_sort(arr: list[int]) -> None:
    for i in range(len(arr) - 1):
        min_idx = i
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[min_idx]:
                min_idx = k
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
selective_sort(arr)
print(arr)
