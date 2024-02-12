N, M = map(int, input().split())
balls = list(map(int, input().split()))

count = 0
for a in range(N - 1):
    for b in range(a + 1, N):
        if balls[a] != balls[b]:
            count += 1

print(count)

"""
5 3
1 3 2 3 2
"""  # 8
"""
8 5
1 5 4 3 2 4 5 2
"""  # 25
