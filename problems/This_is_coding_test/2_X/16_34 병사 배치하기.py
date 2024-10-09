N = int(input())
powers = list(map(int, input().split()))

max_len = [1] * N
for pivot in range(1, N):
    for prev in range(pivot):
        if powers[prev] > powers[pivot]:
            max_len[pivot] = max(max_len[pivot], max_len[prev] + 1)

print(N - max(max_len))
