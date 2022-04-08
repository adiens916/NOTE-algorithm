from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def merge(left: list, right: list) -> list:
    left_len = len(left)
    right_len = len(right)
    # 두 리스트를 합칠 곳
    result = [0] * (left_len + right_len)

    # HACK: append와 pop 말고 인덱스로 처리하기
    a = b = i = 0
    # 두 리스트가 모두 남아있는 한 반복
    while a < left_len and b < right_len:
        if left[a] <= right[b]:
            result[i] = left[a]
            a += 1
        else:
            result[i] = right[b]
            b += 1
        i += 1
    # left가 남아있는 경우엔 left만 추가
    while a < left_len:
        result[i] = left[a]
        a += 1
        i += 1
    # right가 남아있는 경우엔 right만 추가
    while b < right_len:
        result[i] = right[b]
        b += 1
        i += 1
    
    return result


def merge_sort(arr: list) -> list:
    # 종료 조건
    if len(arr) == 1:
        return arr

    # 분할
    # 1. 좌우 <- 좌우로 나눌 절반 위치 구하기
    mid = len(arr) // 2

    # 2. 절반을 중심으로 좌우 리스트 만들기
    # 파이썬은 슬라이싱으로 간편하게 구현!
    left = arr[:mid]
    right = arr[mid:]

    # 3. 마지막으로 각각의 리스트를 또 쪼개고,
    # 리턴으로 결합된 걸 받음
    left = merge_sort(left)
    right = merge_sort(right)

    # 문제 조건 추가: 왼쪽 마지막이 더 큰 경우의 수
    if left[-1] > right[-1]:
        global reversal_count 
        reversal_count += 1

    # 병합
    return merge(left, right)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    reversal_count = 0
    arr = merge_sort(arr)
    print('#{} {} {}'.format(test_case, arr[N//2], reversal_count))
