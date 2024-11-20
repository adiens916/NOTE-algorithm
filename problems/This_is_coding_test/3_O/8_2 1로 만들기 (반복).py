X = int(input())

table = [0] * (X + 1)
table[1] = 0

for i in range(2, X + 1):
    counts = []
    if i % 5 == 0:
        count = table[i // 5] + 1
        counts.append(count)
    if i % 3 == 0:
        count = table[i // 3] + 1
        counts.append(count)
    if i % 2 == 0:
        count = table[i // 2] + 1
        counts.append(count)
    count = table[i - 1] + 1
    counts.append(count)

    table[i] = min(counts)

print(table[X])
