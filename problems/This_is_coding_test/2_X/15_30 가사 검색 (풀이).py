"""
다음에는 Trie 구조로 풀어보기
"""

from bisect import bisect_left, bisect_right


def solution(words, queries):
    # group by length
    # XXX: 숫자를 키로 하는 경우, 딕셔너리 대신 배열 사용
    arr = [[] for _ in range(10001)]
    r_arr = [[] for _ in range(10001)]

    for word in words:
        arr[len(word)].append(word)
        # XXX: 뒤집을 때는 [::-1]
        r_arr[len(word)].append(word[::-1])

    # sort
    for i in range(1, 10001):
        arr[i].sort()
        r_arr[i].sort()

    answer = []
    # count by range
    for q in queries:
        start = q.replace("?", "a")
        end = q.replace("?", "z")

        # if query starts with ?, reverse all
        if q[0] == "?":
            count = count_by_range(r_arr[len(q)], start[::-1], end[::-1])
        else:
            count = count_by_range(arr[len(q)], start, end)
        answer.append(count)

    return answer


def count_by_range(array, start, end):
    start_idx = bisect_left(array, start)
    end_idx = bisect_right(array, end)
    return end_idx - start_idx
