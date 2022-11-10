"""
우선 문자 길이에 맞는 배열을 찾은 후,
그 다음 문자를 사전순으로 비교하며 삽입 정렬함.

=> 시간 초과남. 삽입 정렬의 시간 복잡도로는 역시 부족한 듯.
계산했을 때도 O(logN)은 되어야 했으니까...
"""

from pathlib import Path

parent = Path(__file__).parent
filename = Path(__file__).stem

import sys

sys.stdin = open(f"{parent}/{filename}_input.txt")
input = sys.stdin.readline


def main():
    N = int(input())
    words = [input().rstrip() for _ in range(N)]
    words = list(set(words))

    words_with_len = [(len(word), word) for word in words]
    words_with_len.sort()

    for length, word in words_with_len:
        print(word)


main()
