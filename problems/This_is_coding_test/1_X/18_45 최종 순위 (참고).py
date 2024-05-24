# 위상 정렬로 푼 코드 예시
# https://www.acmicpc.net/source/76999500

import sys

I = sys.stdin.readline

for _ in range(int(I())):
    n = int(I())
    *arr, = map(int, I().split())
    indegree = [0] * (n + 1)
    for i, team in enumerate(arr):
        indegree[team] = i

    indegree_tmp = [0] * (n + 1)
    for _ in range(int(I())):
        a, b = map(int, I().split())
        if indegree[a] > indegree[b]:
            a, b = b, a
        indegree_tmp[a] += 1
        indegree_tmp[b] -= 1
    indegree = [indegree[i] + indegree_tmp[i] for i in range(n + 1)]

    ans = []
    tmp = [(indegree[team], team) for team in range(1, n + 1)]
    tmp.sort()

    c = 0
    for i in range(n):
        if tmp[i][0] != i:
            c = 1
            break

    if c == 1:
        print('IMPOSSIBLE')
    else:
        ans = [t[1] for t in tmp]
        print(*ans)
