N, M = map(int, input().split())
balls = list(map(int, input().split()))

counts = [0] * 11
for ball in balls:
    counts[ball] += 1

case_sum = 0
remains = N
for count in counts[1:]:
    case_sum += count * (remains - count)
    remains -= count

print(case_sum)

"""
5 3
1 3 2 3 2
"""  # 8
"""
9 5
1 2 2 3 3 3 4 4 5

1 * 8 +
2 * 6 +
3 * 3 +
2 * 1
"""  # 31
