"""
이것이 코딩 테스트다 7-2
"""

def binary_search(start, end):
    if start > end:
        return None

    middle = (start + end) // 2
    if arr[middle] > target:
        return binary_search(start, middle - 1)
    elif arr[middle] < target:
        return binary_search(middle + 1, end)
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
"""
