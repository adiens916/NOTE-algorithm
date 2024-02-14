def solution(s):
    min_length = len(s)

    for length in range(2, len(s) // 2):
        answer_len = 0
        anchor = 0

        while True:
            moving = anchor + length

            is_equal = True
            equal_count = 1
            for i in range(len(length)):
                if s[anchor + i] != s[moving + i]:
                    is_equal = False
                    break
            if is_equal:
                moving += length
                equal_count += 1
            else:
                answer_len += len(str(equal_count)) + length
                anchor = moving

        min_length = min(min_length, answer_len)

    answer = min_length
    return answer
