X = int(input())

INF = int(1e9)
table = [INF] * 30001
table[1] = 0


def count_num_to_1(num: int) -> int:
    if table[num] != INF:
        return table[num]

    min_count = INF
    if num % 5 == 0:
        count_by_5 = count_num_to_1(num // 5) + 1
        min_count = min(min_count, count_by_5)
    if num % 3 == 0:
        count_by_3 = count_num_to_1(num // 3) + 1
        min_count = min(min_count, count_by_3)
    if num % 2 == 0:
        count_by_2 = count_num_to_1(num // 2) + 1
        min_count = min(min_count, count_by_2)
    count_by_1 = count_num_to_1(num - 1) + 1
    min_count = min(min_count, count_by_1)

    table[num] = min_count
    return min_count


print(count_num_to_1(X))

"""
26
"""  # 3
