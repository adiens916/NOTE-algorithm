from functools import cmp_to_key
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    name, *scores = input().split()
    scores_num = list(map(int, scores))
    arr.append((name, *scores_num))

T = tuple[str, int, int, int]


def compare_score_then_name(a: T, b: T) -> int:
    # 국어 점수가 감소하는 순서
    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1

    # 국어 점수 같은 경우, 영어 점수가 증가하는 순서
    if a[2] < b[2]:
        return -1
    elif a[2] > b[2]:
        return 1

    # 영어 점수 같은 경우, 수학 점수 감소하는 순서
    if a[3] < b[3]:
        return 1
    elif a[3] > b[3]:
        return -1

    # 점수가 같은 경우, 이름이 사전 순으로 증가하는 순서
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    return 0


result = sorted(arr, key=cmp_to_key(compare_score_then_name))
print(*[e[0] for e in result], sep='\n')

"""
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""