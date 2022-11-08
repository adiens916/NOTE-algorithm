"""
삽입 정렬
"""

# from pathlib import Path

# parent = Path(__file__).parent
# filename = Path(__file__).stem
# sys.stdin = open(f"{parent}/{filename}_input.txt")

from pprint import pprint
import sys

input = sys.stdin.readline


MAX_LEN = 20


def main():
    N = int(input())
    words = [input().rstrip() for _ in range(N)]
    sorted_words = sort_words_by_length(words, N)
    print("\n".join(sorted_words))


def sort_words_by_length(words: list[str], N) -> list[str]:
    words_by_len = [[""] * N for _ in range(MAX_LEN + 1)]

    for word in words:
        for index in range(N):
            pass


main()
