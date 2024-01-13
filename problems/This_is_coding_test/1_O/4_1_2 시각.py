def count_target_num_until_nth_of_clock(target_num: int, n: int) -> int:
    basic_count = 0

    for m in range(60):
        for s in range(60):
            if str(target_num) in str(m) or str(target_num) in str(s):
                basic_count += 1

    count = 0

    for h in range(n + 1):
        if str(target_num) not in str(h):
            count += basic_count
        else:
            count += 3600

    return count


N = int(input())
print(count_target_num_until_nth_of_clock(3, N))
