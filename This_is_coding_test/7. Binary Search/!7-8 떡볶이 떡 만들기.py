"""
- 파라메트릭 서치(Parametric Search) 유형.
: 최적화 문제를 결정 문제 (예 / 아니오 문제)로 바꿔 해결하는 기법.
'원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 파라메트릭 서치 사용.

예) 범위 내 최댓값 => 이진 탐색(예 / 아니오)로 판단하고 범위 좁혀나감

- 시간 복잡도
10억 => log 취하면 약 30번 정도 높이 비교
* 최대 100만개 잘린 떡 높이 구하기
=> 최대 3000만 => 2초 안에 계산 가능
"""

def sum_remains(cut_height):
    """
    잘리고 남은 떡의 전체 총합 구하기
    """
    remain_sum = 0
    for stick in sticks:
        remain = stick - cut_height
        if remain > 0:
            remain_sum += remain
    return remain_sum


def binary_search():
    """
    절단기 최대 높이 찾기
    """
    start = 0
    end = max(sticks)

    while start <= end:
        mid = (start + end) // 2
        remain_sum = sum_remains(mid)

        # 잘린 떡의 길이가 부족한 경우
        if remain_sum < M:
            # 절단기 높이 낮추기
            end = mid - 1
        # 잘린 떡이 충분하면
        else:
            # 높이 최대치 갱신
            cur_max = mid
            start = mid + 1
    
    return cur_max


N, M = map(int, input().split())
sticks = list(map(int, input().split()))
cur_max = binary_search()
print(cur_max)

"""
4 6
19 15 10 17
"""
