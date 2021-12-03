# NOTE: swap 대신 index만 교체하는 게 더 값쌈.

def selection_sorting(arr):
    N = len(arr)
    for i in range(0, N - 1):
        min_index = i
        for j in range(i + 1, N):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
selection_sorting(arr)
print(arr)
