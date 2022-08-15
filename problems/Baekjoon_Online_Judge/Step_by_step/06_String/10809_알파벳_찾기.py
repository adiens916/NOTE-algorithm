"""https://www.acmicpc.net/problem/10809"""

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


# 문자열 입력
S = input().rstrip()
# 알파벳 개수만큼의 배열 생성
alphabets = [-1] * (ord('z') - ord('a') + 1)

for i in range(len(S)):
    # 현재 문자의 알파벳 순서
    index = ord(S[i]) - ord('a')
    # 해당 알파벳이 알파벳 배열에 없던 경우
    if alphabets[index] == -1:
        # 알파벳이 처음 등장하는 위치를 배열에 저장
        alphabets[index] = i

print(*alphabets, sep=' ')
