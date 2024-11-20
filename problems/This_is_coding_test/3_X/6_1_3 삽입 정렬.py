def insertion_sort(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        for k in range(i, 0, -1):
            if arr[k - 1] > arr[k]:
                arr[k - 1], arr[k] = arr[k], arr[k - 1]
            else:
                break


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
insertion_sort(arr)
print(arr)