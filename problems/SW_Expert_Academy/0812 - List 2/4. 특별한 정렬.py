"""
일부러 카운팅 정렬 중 카운팅만 이용해서 풀어봤다.
왜냐하면 전체 정렬할 필요없이 일부 값만 필요하기 때문이다.

그러나 생각보다 엄청 빠른 것도 아니었다. (평균 수준)
이론적으로는 더 빠를 텐데 왜지?...

10*log10  vs.  10+100
30 vs. 110

100*log100 vs. 100+100
1000 vs. 200

: N이 작아서 그런가보다.
"""


from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    print("#{}".format(test_case), end=" ")

    N = int(input())
    numbers = list(map(int, input().split()))
    number_counts = [0] * 101

    # 카운팅 정렬 중 카운팅만 수행
    for i in range(N):
        number_counts[numbers[i]] += 1
    max_idx = 100
    min_idx = 1
    # 최대 최소 갱신
    while number_counts[max_idx] == 0:
        max_idx -= 1
    while number_counts[min_idx] == 0:
        min_idx += 1

    # 홀수 자리는 최대를, 짝수 자리는 최소를 찍음
    for i in range(10):
        if i % 2 == 0:
            number = max_idx
            # 최대 정수 하나 제거
            number_counts[max_idx] -= 1
            # 중복일 수도 있으므로 다시 한번 체크
            while number_counts[max_idx] == 0 and min_idx < max_idx:
                max_idx -= 1
        else:
            number = min_idx
            number_counts[min_idx] -= 1
            # FIXME: max가 전부 지워져서 min이 계속 올라가는 경우 있었음
            # min이 max보다 작은 한에서만 체크해야 함
            while number_counts[min_idx] == 0 and min_idx < max_idx:
                min_idx += 1
        print(number, end=" ")
    print()
