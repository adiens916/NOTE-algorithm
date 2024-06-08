N, M = map(int, input().split())
sticks = list(map(int, input().split()))

start = 0
end = max(sticks)
max_height = 0

while start <= end:
    mid = (start + end) // 2

    cur_stick_sum = 0
    for stick in sticks:
        if stick > mid:
            cur_stick_sum += stick - mid

    if cur_stick_sum >= M:
        max_height = max(max_height, mid)
        start = mid + 1
    else:
        end = mid - 1

print(max_height)

"""
4 6
19 15 10 17
"""  # 15
