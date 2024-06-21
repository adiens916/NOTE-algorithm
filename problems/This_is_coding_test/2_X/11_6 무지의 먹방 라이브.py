INF = int(1e9)


def get_common_time_and_count(food_times: list[int]):
    count = 0
    common_time = INF
    for t in food_times:
        if t > 0:
            count += 1
            # XXX: 무조건 최솟값으로 갱신
            common_time = min(t, common_time)
    return common_time, count


def solution(food_times, k):
    while k > 0:
        common_time, count = get_common_time_and_count(food_times)
        consumed = common_time * count

        if consumed >= k:
            # XXX: 남은 시간 % 남은 개수만큼 나누기
            pos = k % count
            for i in range(len(food_times)):
                if food_times[i] == 0:
                    continue
                pos -= 1
                if pos <= 0:
                    return i + 1

        else:
            # 시간 줄이기
            for i in range(len(food_times)):
                if food_times[i] > 0:
                    food_times[i] -= common_time
            k -= consumed


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
"""  # 2
"""
3 5 1
5
"""  # 1
