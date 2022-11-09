"""
우선 문자 길이에 맞는 배열을 찾은 후,
그 다음 문자를 사전순으로 비교하며 삽입 정렬함.
"""

from pathlib import Path

parent = Path(__file__).parent
filename = Path(__file__).stem

import sys

sys.stdin = open(f"{parent}/{filename}_input.txt")
input = sys.stdin.readline


MAX_LEN = 50


def main():
    N = int(input())
    words = [input().rstrip() for _ in range(N)]
    sorted_words = sort_words_by_length(words, N)

    for word_list in sorted_words[1:]:
        for word in word_list:
            if word:
                print(word)
            else:
                break


def sort_words_by_length(words: list[str], N) -> list[str]:
    words_by_len = [[""] * N for _ in range(MAX_LEN + 1)]

    for word in words:
        length = len(word)
        for i in range(N):
            comp_word = words_by_len[length][i]
            # 배열의 빈 곳에는 무조건 넣음
            # 예시: 맨 처음, 맨 마지막인 경우 등
            if comp_word == "":
                words_by_len[length][i] = word
                break
            # 중복이면 넘어감
            elif word == comp_word:
                break
            # 비교 중인 단어보다 사전순으로 먼저 오는 경우
            elif word < comp_word:
                # 삽입 정렬 이용
                inserting = word
                for j in range(i, N):
                    # 기존 단어 보존
                    preserving = words_by_len[length][j]
                    if inserting:
                        # 기존 위치에 새 단어 넣음
                        words_by_len[length][j] = inserting
                        # 새로 넣을 단어를 아까 보존했던 단어로 바꿈
                        inserting = preserving
                    else:
                        break
                break

    return words_by_len


main()
