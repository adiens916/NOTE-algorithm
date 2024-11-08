N, K = map(int, input().split())

count = 0
while N > 1:
    remains = N % K
    if remains != 0:
        N -= remains
        count += remains
    else:
        N = N // K
        count += 1

print(count)
