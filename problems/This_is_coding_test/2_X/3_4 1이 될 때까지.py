N, K = map(int, input().split())

count = 0
while N > 1:
    remains = N % K
    if remains == 0:
        N //= K
        count += 1
    else:
        N -= remains
        count += remains

print(count)


"""
25 5
"""  # 2
"""
17 4
"""  # 3
