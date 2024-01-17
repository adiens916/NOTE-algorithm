def insertion_sort(arr: list[int]) -> list[int]:
    for start in range(1, len(arr)):
        for pivot in range(start, 0, -1):
            if arr[pivot] < arr[pivot - 1]:
                arr[pivot], arr[pivot - 1] = arr[pivot - 1], arr[pivot]
            else:
                break
    return arr


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(insertion_sort(arr))
