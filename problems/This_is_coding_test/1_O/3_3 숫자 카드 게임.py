N, M = map(int, input().split())

prev_min = 0
for i in range(N):
    arr = list(map(int, input().split()))
    cur_min = min(arr)
    if cur_min > prev_min:
        prev_min = cur_min

print(prev_min)
