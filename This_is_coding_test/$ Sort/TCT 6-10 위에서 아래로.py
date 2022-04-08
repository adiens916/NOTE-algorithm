"""
내림차순 정렬하기
"""

def selection_sort(arr, N):
    for put in range(N - 1):
        max_idx = put
        for pick in range(put + 1, N):
            if arr[max_idx] < arr[pick]:
                max_idx = pick
        arr[put], arr[max_idx] = arr[max_idx], arr[put]


N = int(input())
arr = [int(input()) for _ in range(N)]
selection_sort(arr, N)
print(*arr)
