from main import TestCaseComparer
from element import IntList, Int


def solution1():
    food_times = list(map(int, input().split()))
    k = int(input())

    # XXX: 불가능한 조건 처리
    if sum(food_times) <= k:
        return -1

    arr = [(food_times[i], i + 1) for i in range(len(food_times))]
    arr.sort()

    prev_time = 0
    for i in range(len(arr)):
        t, no = arr[i]
        remains = len(arr) - i
        consumed = (t - prev_time) * remains

        # XXX: 같은 경우에도 일단 전부 다 돌 수 있음.
        if consumed <= k:
            k -= consumed
            prev_time = t
        else:
            # 남은 것들의 순서 구하기
            arr_by_no = sorted(arr[i:], key=lambda x: x[1])
            # 남은 시간 % 남은 것들 개수 = 남은 것들 중 몇 번째인지
            pos = k % len(arr_by_no)
            return arr_by_no[pos][1]


def solution2():
    food_times = list(map(int, input().split()))
    k = int(input())

    if sum(food_times) <= k:
        return -1

    foods = [(food_times[i], i) for i in range(len(food_times))]

    foods.sort()
    prev_t = 0
    for i in range(len(foods)):
        cur_t = foods[i][0] - prev_t
        remain_num = len(foods) - i
        total_t = cur_t * remain_num

        if total_t <= k:
            k -= total_t
            # XXX: 이 부분이 틀린 부분. 원래는 prev_t = foods[i][0]이어야 함.
            prev_t = cur_t
        else:
            foods = foods[i:]
            break

    foods.sort(key=lambda x: x[1])
    # XXX: 나머지 연산 필요했음.
    # 총합으로만 비교했는데, 개수는 적고 음식량이 많을 수 있기 때문.
    target = k % len(foods)
    answer = foods[target][1]
    return answer + 1


food_inputs = IntList(1, 100, 1, 5)
k_input = Int(1, 100)
template = [
    [food_inputs],
    [k_input]
]

cmp = TestCaseComparer()
cmp.set_template(template)
cmp.add(solution1)
cmp.add(solution2)
cmp.compare(n = 100)

"""
Test Case 20:
Input: 12 55 25 17 18
91
Result1: 2
Method 'solution2' DIFFERENT:
Result2: 5
"""