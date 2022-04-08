from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def three_way_partition(arr: list, pivot: int, small: int, large: int):
    # 맨 처음부터 우측으로 이동하면서
    # 작은 것들 / 같은 것들 / 큰 것들로 나누는 방식

    # 맨 좌측 작은 쪽부터 시작해서 큰 쪽 영역과 접할 때까지 비교
    point = small
    while point <= large:
        # 현재 위치 값 < 기준
        if arr[point] < pivot:
            # 좌측은 같은 값들의 시작 부분이다.  예) {3} 3 1
            # 그러므로 현재 작은 값을 좌측으로 보내고  예) 1 <-
            # 좌측의 같은 값을 현재 위치로 옮겨오면  예) 3 ->
            # 정렬된 순서가 된다.  예) 1 3 {3}
            arr[small], arr[point] = arr[point], arr[small]
            # 현재 위치는 끝났으므로, 둘 다 다음 자리로 이동
            small += 1
            point += 1
        elif arr[point] > pivot:
            # 우측은 같은 값들의 끝 부분이자, 큰 값들의 이전 부분이다.
            # 그러므로 현재 큰 값을 우측으로 보내고
            # 우측에 있던 값을 현재 위치로 가져오면
            # 적어도 큰 값을 우측에 하나 확실히 보내게 된다.
            arr[point], arr[large] = arr[large], arr[point]
            # 새로운 값도 큰 값일 수 있으므로,
            # 현재 위치를 다시 한번 비교해야 한다.
            # 따라서 큰 값의 이전 부분만 한 칸 당긴다.
            large -= 1
        else:
            # 같은 값인 경우, 이미 정렬된 상태이므로, 그대로 다음 위치로 간다.
            point += 1
    
    # 작은 값들의 끝 부분과, 큰 값들의 시작 부분을 반환
    return small - 1, large + 1


def quick_sort(arr, start, end):
    # 최소 2개 이상을 정렬할 수 있는 경우
    if start < end:
        # 가운데 위치한 값을 기준으로 함
        mid = (start + end) // 2
        pivot = arr[mid]

        # (작은 것들) (같은 것들) (큰 것들)로 분할 및 정렬한 후,
        # 작은 것들의 경계 지점과, 큰 것들의 경계 지점을 반환
        small, large = three_way_partition(arr, pivot, start, end)

        # 작은 것들 처음 ~ 작은 것들 끝까지 정렬
        quick_sort(arr, start, small)
        # 큰 것들 처음 ~ 큰 것들 끝까지 정렬
        quick_sort(arr, large, end)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N - 1)
    print('#{} {}'.format(test_case, arr[N//2]))
