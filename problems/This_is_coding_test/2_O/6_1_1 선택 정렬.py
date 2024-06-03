def selection_sort(arr: list[int]) -> None:
    for start in range(len(arr) - 1):
        for i in range(start + 1, len(arr)):
            if arr[start] > arr[i]:
                # XXXL 배열 원소를 여러 번 바꾸느라 비효율적
                arr[start], arr[i] = arr[i], arr[start]


# 책 예제
def selection_sort_2(arr: list[int]) -> None:
    for start in range(len(arr) - 1):
        min_index = start
        for i in range(start + 1, len(arr)):
            if arr[min_index] > arr[i]:
                min_index = i
        # XXX: 한 번만 바꿀 수 있으므로 좀 더 효율적
        arr[start], arr[min_index] = arr[min_index], arr[start]


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
selection_sort(arr)
print(arr)
