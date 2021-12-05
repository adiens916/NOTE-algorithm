# NOTE: swap 대신 index만 교체하는 게 더 값쌈.

def selection_sorting(arr):
    N = len(arr)
    for put in range(0, N - 1):
        min_index = put
        for pick in range(put + 1, N):
            if arr[min_index] > arr[pick]:
                min_index = pick
        arr[put], arr[min_index] = arr[min_index], arr[put]


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
selection_sorting(arr)
print(arr)
