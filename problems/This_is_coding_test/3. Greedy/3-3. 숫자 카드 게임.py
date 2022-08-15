N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cur_max = 0
for row in arr:
    cur_min = min(row)
    if cur_min > cur_max:
        cur_max = cur_min

print(cur_max)
