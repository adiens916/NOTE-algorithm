"""
이것이 코딩 테스트다 7-3
"""

def binary_search(start, end):
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] > target:
            end = middle - 1
        elif arr[middle] < target:
            start = middle + 1
        else:
            return middle


N, target = map(int, input().split())
arr = list(map(int, input().split()))

target_idx = binary_search(0, N - 1)
if target_idx:
    print(target_idx)
else:
    print('원소가 존재하지 않습니다.')

"""
10 7
1 3 5 7 9 11 13 15 17 19

10 7
1 3 5 6 9 11 13 15 17 19
"""