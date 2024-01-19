N, M = map(int, input().split())
stick_list = list(map(int, input().split()))

start = 0
end = max(stick_list)
max_height = 0

while start <= end:
    mid = (start + end) // 2

    remains = 0
    for stick in stick_list:
        if stick > mid:
            remains += stick - mid

    if remains > M:
        # XXX: 항상 최적화된 값을 찾기 때문에, max할 필요 없음.
        # 그냥 계속 mid 값으로 갱신하면 됨.
        max_height = max(max_height, mid)
        start = mid + 1
    elif remains < M:
        end = mid - 1
    else:
        break

print(mid)


"""
4 6
19 15 10 17
"""
