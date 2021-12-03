"""
- 데이터가 거의 정렬된 상태일 때 강력함
<- 필요할 때만 위치를 바꾸기 때문

- 정렬이 이루어진 원소는 어느 단계든 오름차순 유지
-> 비교하려면 특정 크기까지만 비교하면 됨
"""

def insertion_sort(arr):
    N = len(arr)

    for p in range(1, N):
        val = arr[p]
        for q in range(p - 1, -1, -1):
            if arr[q] > val:
                arr[q+1] = arr[q]
            else:
                break
        arr[q+1] = val


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
insertion_sort(arr)
print(arr)