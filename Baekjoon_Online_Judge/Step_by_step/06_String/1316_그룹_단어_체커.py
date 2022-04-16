"""https://www.acmicpc.net/problem/1316"""

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


def is_group_word(string: str):
    char_set = set()
    # 첫 글자는 일단 등록
    char_set.add(string[0])

    # 두 번째 글자부터 끝 글자까지
    for i in range(1, len(string)):
        # 이전 글자와 다른 경우
        if string[i] != string[i - 1]:
            # 처음 등장한 글자인 경우면 괜찮음
            if string[i] not in char_set:
                char_set.add(string[i])
            # 이전에 등장했던 글자면 그룹 단어 X
            else:
                return False
    return True


N = int(input())
count = 0

for _ in range(N):
    string = input().rstrip()
    if is_group_word(string):
        count += 1
    # if list(word) == sorted(word, key=word.find):
    #     result += 1

print(count)