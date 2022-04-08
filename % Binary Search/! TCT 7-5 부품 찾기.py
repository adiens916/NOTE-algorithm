"""
N개에서 M개 찾는 문제

- 이진 탐색 => O(N log N) == 2000만
- 계수 정렬 => O(N + M) == 100만
- 집합 => O(1)
    : '단순히 특정 수가 한 번이라도 등장했는지만 검사하므로 가능'
"""

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2
        if arr[middle] > target:
            end = middle - 1
        elif arr[middle] < target:
            start = middle + 1
        else:
            return True
    return False


def counting():
    full_range = [False] * 1000001
    for candidate in candidates:
        full_range[candidate] = True

    for target in targets:
        if full_range[target]:
            print('yes', end=' ')
        else:
            print('no', end=' ')


N = int(input())
candidates = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

### 1. binary search
# for target in targets:
#     found = binary_search(candidates, target)
#     if found:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

### 2. counting sort
# counting()

### 3. set
# candidate_set = set(candidates)
# for target in targets:
#     if target in candidate_set:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

"""
5
8 3 7 9 2
3
5 7 9
"""