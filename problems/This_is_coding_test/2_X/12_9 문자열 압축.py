# Counter도 안 됨. 중간에 낄 수 있음.
# 처음부터 끝까지 탐색 필요.


def solution(s):
    cur_total_count = 1000
    for length in range(1, len(s) // 2 + 1):
        total_count = 0
        start = 0
        count = 1

        while start < len(s):
            prev = s[start : start + length]
            nxt = s[start + length : start + length * 2]

            if prev == nxt:
                count += 1
            else:
                total_count += len(prev) + (len(str(count)) if count > 1 else 0)
                count = 1
                prev = nxt

            start += length

        cur_total_count = min(cur_total_count, total_count)

    answer = cur_total_count
    return answer


print(solution("a"))
