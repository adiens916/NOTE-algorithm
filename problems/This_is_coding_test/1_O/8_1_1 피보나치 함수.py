def fibonacci(n: int, level: int) -> int:
    # XXX: 호출 횟수 표시
    indent = "  " * level + "└" + "─"
    print(f"{indent}f({n})")

    if n <= 1:
        return n

    return fibonacci(n - 1, level + 1) + fibonacci(n - 2, level + 1)


fibonacci(20, 0)
