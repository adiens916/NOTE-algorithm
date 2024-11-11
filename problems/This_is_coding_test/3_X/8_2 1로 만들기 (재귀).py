def count_to_reduce_to_1(n: int, table: list[int]) -> int:
    # XXX: 1일 때 조건도 필요
    if n == 1 or table[n]:
        return table[n]
    else:
        counts = []
        if n % 5 == 0:
            count = count_to_reduce_to_1(n // 5, table)
            counts.append(count + 1)
        if n % 3 == 0:
            count = count_to_reduce_to_1(n // 3, table)
            counts.append(count + 1)
        if n % 2 == 0:
            count = count_to_reduce_to_1(n // 2, table)
            counts.append(count + 1)
        count = count_to_reduce_to_1(n - 1, table)
        counts.append(count + 1)

        table[n] = min(counts)
        return table[n]


X = int(input())

table = [0] * (X + 1)
table[1] = 0

answer = count_to_reduce_to_1(X, table)
print(answer)
