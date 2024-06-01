def selection_sort(arr: list[int]) -> list[int]:
    for pivot in range(len(arr) - 1):
        min_index = pivot

        for moving in range(pivot + 1, len(arr)):
            if arr[min_index] > arr[moving]:
                min_index = moving

        arr[pivot], arr[min_index] = arr[min_index], arr[pivot]

    return arr


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(selection_sort(arr))
