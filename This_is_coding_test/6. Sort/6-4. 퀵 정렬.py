def partition(start, end):   
    # 피벗 설정
    middle = (end + start) // 2
    pivot = arr[middle]
    arr[middle], arr[start] = arr[start], arr[middle]

    left = start
    right = end

    # 정상 범위 보장
    while True:
        # 인덱스 보장 & 큰 값 나오면 멈춤
        while left <= end and arr[left] <= pivot:
            left += 1
        # 인덱스 보장 & 작은 값 나오면 멈춤
        while start <= right and arr[right] > pivot:
            right -= 1
        
        # 정상 범위인 경우, 큰 값과 작은 값 위치 교환
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        # 범위가 역전되면 교환 중지
        else:
            # 피벗이랑 작은 값 끝이랑 위치 교환
            arr[start], arr[right] = arr[right], arr[start]

            # 새 구간 반환
            return right - 1, left 


def quicksort(start, end):
    # FIXME: 정상 범위 보장
    if start < end:
        new_end, new_start = partition(start, end)
        quicksort(start, new_end)
        quicksort(new_start, end)


arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quicksort(0, len(arr) - 1)
print(arr)
