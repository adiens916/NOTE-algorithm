def nTTr(n, r, k):
    if k == r:
        if sum(case) == M:
            print(*case)
    else:
        for i in range(1, n + 1):
            case[k] = i
            nTTr(n, r, k + 1)


N, M = map(int, input().split())
case = [0] * N
nTTr(6, N, 0)
