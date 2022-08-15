"""https://www.acmicpc.net/problem/4673"""

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


# 생성자 함수
def generate_self_number(x):
    # 자기 자신 + 문자열 리스트로 쪼개서 자릿수 더하기
    return x + sum(map(int, list(str(x))))


number_set = set()
for i in range(1, 10001):
    # 여태까지 나온 적이 없던 경우,
    if i not in number_set:
        # 처음 나온 숫자이므로 출력
        print(i)

        x = i
        # 나온 적이 없으면서 10000보다 작거나 같은 경우
        while x not in number_set and x <= 10000:
            # 나온 적 있다고 표시 (세트에 추가)
            number_set.add(x)
            # 생성자를 이용하여 수 교체
            x = generate_self_number(x)
