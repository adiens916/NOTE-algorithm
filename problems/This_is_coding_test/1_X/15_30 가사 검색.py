"""
이진 탐색으로 시작 지점과 끝 점 찾기
- 앞이 소문자면 그대로 이진 탐색
- 앞이 ?면 뒤집고, words들도 뒤집어서 찾기
- 전부 ?면 그냥 배열 길이만 저장하기
"""
from bisect import bisect_left, bisect_right


def solution(words, queries):
    # words들은 글자 수로 분류 & 뒤집기도 필요
    reversed_words = get_reversed_words(words)
    reversed_words.sort()
    r_words_by_len = get_words_by_len(reversed_words)

    words.sort()
    words_by_len = get_words_by_len(words)

    # query는 중복된다고 했으니, 테이블에 저장
    table = dict()
    answer = []
    for query in queries:
        if table.get(query) is None:
            # 전부 다 ?인 경우
            if query[0] == '?' and query[-1] == '?':
                count = len(words_by_len[len(query)])
            # 접미사가 ?인 경우
            elif query[0] != '?':
                count = count_word(words_by_len[len(query)], query)
            # 접두사가 ?인 경우
            elif query[-1] != '?':
                count = count_word(r_words_by_len[len(query)], query[-1::-1])

            table[query] = count

        answer.append(table.get(query))

    return answer


def get_words_by_len(words: list) -> list:
    words_by_len = [[] for _ in range(10001)]
    for word in words:
        words_by_len[len(word)].append(word)
    return words_by_len


def get_reversed_words(words: list) -> list:
    reversed_words = []
    for word in words:
        reversed_words.append(word[-1::-1])
    return reversed_words


def count_word(words: list, query: str) -> int:
    # 이진 탐색으로 시작 지점과 끝 점 찾기
    start = bisect_left(words, query.replace('?', 'a'))
    end = bisect_right(words, query.replace('?', 'z'))
    return end - start


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))  # [3, 2, 4, 1, 0]
