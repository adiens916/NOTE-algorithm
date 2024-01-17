def selection_sort_reversed(arr: list[int]) -> list[int]:
    for pivot in range(len(arr) - 1):
        max_index = pivot

        for moving in range(pivot + 1, len(arr)):
            if arr[max_index] < arr[moving]:
                max_index = moving

        arr[pivot], arr[max_index] = arr[max_index], arr[pivot]

    return arr


N = int(input())
arr = [int(input()) for _ in range(N)]
print(*selection_sort_reversed(arr), sep=" ")

"""
3
15
27
12
"""
