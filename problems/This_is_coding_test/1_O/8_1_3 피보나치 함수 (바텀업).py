memo = [0] * (100 + 1)

memo[0] = 0
memo[1] = 1
memo[2] = 1
for i in range(3, 101):
    memo[i] = memo[i - 1] + memo[i - 2]


def fibonacci_iter(n: int) -> int:
    return memo[n]


print(fibonacci_iter(20))
