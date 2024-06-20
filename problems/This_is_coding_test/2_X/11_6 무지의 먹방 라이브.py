from collections import deque


def solution(food_times, k):
    arr = [(food_times[i], i) for i in range(len(food_times))]
    arr = deque(sorted(arr))

    while k > 0:
        common_time = arr[0][0]
        count = len(arr)
        consumed = common_time * count

        if consumed >= k :
            pos = consumed % k
            return pos + 1

        count = 0
        for i in range(len(arr)):
            remains = arr[i][0] - common_time
            if remains == 0:
                count += 1
            else:
                arr[i] = (remains, arr[i][1])
        for _ in range(count):
            arr.popleft()

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
"""
