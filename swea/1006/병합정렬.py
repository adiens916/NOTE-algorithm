def merge(left: list, right: list):
    # 두 리스트를 합치기
    result = []

    # 두 리스트가 모두 남아있는 한 반복
    while left and right:
        if left[0] <= right[0]:
            # pop 말고 인덱스로 처리하기
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        # 1) 하나씩 복사
        # while left:
        #     result.append(left.pop(0))
        # 2) 한번에 나머지를 뒤에 추가
        result.extend(left)
        left.clear()
    else:  # right
        result.extend(right)
        right.clear()

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

    # 병합
    return merge(left, right)


"""
69 10 28 14 60 50 -10 20
"""

N = int(input())
arr = list(map(int, input().split()))
arr = merge_sort(arr)
print(arr)