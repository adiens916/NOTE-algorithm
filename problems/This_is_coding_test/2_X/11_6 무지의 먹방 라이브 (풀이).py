def solution(food_times, k):
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


food_times = list(map(int, input().split()))
k = int(input())
print(solution(food_times, k))

"""
3 1 2
5
"""  # 1
"""
2 2 2
5
"""  # 3
"""
3 5 1
5
"""  # 1
"""
1 2
2
"""
