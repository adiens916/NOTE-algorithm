dp_table = [0] * 100


def fibonacci(N):
    dp_table[1] = dp_table[2] = 1
    i = 3
    while i <= N:
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]
        i += 1


fibonacci(99)
print(dp_table[99])