memo = [0] * (100 + 1)


def fibonacci_dp(n: int, level: int) -> int:
    # XXX: 호출 횟수 표시
    indent = "  " * level + "└" + "─"
    print(f"{indent}f({n})")

    if n <= 1:
        return n

    if memo[n] == 0:
        memo[n] = fibonacci_dp(n - 1, level + 1) + fibonacci_dp(n - 2, level + 1)

    return memo[n]


print(fibonacci_dp(20, 0))
