N = int(input())
fears = list(map(int, input().split()))

# 계수 정렬 응용
fear_counts = [0] * (N + 1)
for fear in fears:
    fear_counts[fear] += 1

# 가장 공포도가 작은 모험가끼리 묶어서 내보내기
group_count = 0
for i in range(1, N + 1):
    while fear_counts[i] >= i:
        fear_counts[i] -= i
        group_count += 1

print(group_count)

"""
5
2 3 1 2 2
"""
