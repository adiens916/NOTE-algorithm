memo = [0] * (30000 + 1)


def count_min_operation_to_make_any_number_to_one(n: int, op: int) -> int:
    if n == 1:
        return op

    if memo[n] != 0:
        return memo[n]

    # XXX: 최솟값을 세팅하는 방법이 임의적임... -> 바텀없으로 하면 됨.
    min_op = int(1e9)
    next = 0
    for div in (5, 3, 2):
        if n % div == 0:
            next = n // div
            cur_op = count_min_operation_to_make_any_number_to_one(next, op + 1)
            min_op = min(min_op, cur_op)
    if next == 0:
        next = n - 1
        cur_op = count_min_operation_to_make_any_number_to_one(next, op + 1)
        min_op = min(min_op, cur_op)

    memo[n] = min_op
    return memo[n]


X = int(input())
print(count_min_operation_to_make_any_number_to_one(X, 0))
