# Counter도 안 됨. 중간에 낄 수 있음.
# 처음부터 끝까지 탐색 필요.


def solution(s):
    cur_total_count = 1000

    # XXX: 최대 범위는 절반까지
    mid = len(s) // 2
    for length in range(1, mid + 1):
        total_count = 0
        start = 0
        count = 1

        while start < len(s):
            # XXX: Python은 범위에 관대하니, 다른 걸로 풀기
            prev = s[start : start + length]
            nxt = s[start + length : start + length * 2]

            if prev == nxt:
                count += 1
            else:
                # XXX: 뒤에 오는 if문의 범위는 ()로 묶어야 함.
                total_count += len(prev) + (len(str(count)) if count > 1 else 0)
                count = 1
                prev = nxt

            start += length

        cur_total_count = min(cur_total_count, total_count)

    answer = cur_total_count
    return answer


print(solution("a"))
