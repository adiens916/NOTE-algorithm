"""
삽입 정렬

- 데이터가 거의 정렬된 상태일 때 강력함
<- 필요할 때만 위치를 바꾸기 때문

- 정렬이 이루어진 원소는 어느 단계에서든 오름차순 유지
-> 비교하려면 특정 크기까지만 비교하면 됨

- 인접한 두 개끼리 swap하는 것보다,
선택 정렬처럼 기준 값을 놓고 비교하는 게 2배 이상 빠름
"""
import time
import random


def insertion_sort_simple(arr):
    N = len(arr)
    for pick in range(1, N):
        for put in range(pick - 1, -1, -1):
            if arr[put + 1] < arr[put]:
                arr[put + 1], arr[put] = arr[put], arr[put + 1]
            else:
                break


def insertion_sort(arr):
    N = len(arr)

    for pick in range(1, N):
        pick_value = arr[pick]
        for put in range(pick - 1, -1, -1):
            if arr[put] > pick_value:
                arr[put + 1] = arr[put]
            else:
                arr[put + 1] = pick_value
                break
        else:
            arr[0] = pick_value



arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# insertion_sort_simple(arr)
# print(arr)

### 속도 비교
big_arr = list(range(1000))
random.shuffle(big_arr)

# overwrite
start = time.time()
insertion_sort(big_arr[:])
end = time.time()
print(end-start)

# swap
start = time.time()
insertion_sort_simple(big_arr[:])
end = time.time()
print(end-start)
