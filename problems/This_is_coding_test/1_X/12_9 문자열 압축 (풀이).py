def compress(s: str, step: int) -> str:
    compressed = ""
    prev = s[0:step]
    count = 1

    for i in range(step, len(s), step):
        if prev == s[i : i + step]:
            count += 1
        else:
            if count > 1:
                compressed += str(count) + prev
            else:
                compressed += prev

            prev = s[i : i + step]
            count = 1

    return compressed


def solution(s: str) -> int:
    answer = len(s)

    mid = len(s) // 2
    for step in range(1, mid + 1):
        compressed = compress(s, step)
        answer = min(answer, len(compressed))

    return answer
