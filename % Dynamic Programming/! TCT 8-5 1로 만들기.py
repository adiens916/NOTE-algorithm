"""
탑-다운 방식으로 풀었으나, 바텀-업도 가능함.
"""

def count_to_one(N):
    if N == 1:
        return 0

    if not mem[N]:
        count_by_5 = INF
        if N % 5 == 0:
            count_by_5 = count_to_one(N // 5)
        
        count_by_3 = INF
        if N % 3 == 0:
            count_by_3 = count_to_one(N // 3)

        count_by_2 = INF
        if N % 2 == 0:
            count_by_2 = count_to_one(N // 2)

        count_by_1 = count_to_one(N - 1)

        mem[N] = min(count_by_5, count_by_3, count_by_2, count_by_1) + 1
    return mem[N]


def count_to_one_by_bottom_up(N):
    for i in range(2, N + 1):
        # 1을 뺀 경우
        dp_table[i] = dp_table[i - 1] + 1
        # 2로 나눈 경우랑 비교
        if i % 2 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i // 2] + 1)
        # 3으로 나눈 경우랑 비교
        if i % 3 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i // 3] + 1)
        # 5로 나눈 경우랑 비교
        if i % 5 == 0:
            dp_table[i] = min(dp_table[i], dp_table[i // 5] + 1)


X = int(input())

mem = [0] * (X + 1)
INF = 1e9
print(count_to_one(X))

dp_table = [0] * (X + 1)
count_to_one_by_bottom_up(X)
print(dp_table[X])