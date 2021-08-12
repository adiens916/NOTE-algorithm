"""
reduce를 안 쓰면 270ms,
안 쓰면 180ms
-> reduce는 되도록 쓰지 말자
"""


from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def powerset(S):
    """
    N개의 원소를 갖는 집합의 멱집합 반환

    전체 부분집합의 개수 == 2^N
    각 부분집합을 0부터 2^N - 1까지 번호를 매김
    이 번호를 이진법으로 나타내면 001010 등으로 나옴
    이 이진수 각 자리에 따라 원소 포함 여부 결정
    1이면 원소 포함, 0이면 원소 미포함
    """
    powerset = []
    N = len(S)

    for subset_num in range(1, 2 ** N):
        subset = []
        # N == 원소의 개수 == 비트 자릿수
        # 원소의 개수와 대응하는 비트 자릿수에 대해
        for bit in range(N):
            # 원소를 포함 == 비트 자릿수가 1
            if subset_num & (1 << bit):
                # 비트 자릿수에 해당하는 원소를 집어넣음
                subset.append(S[bit])
        powerset.append(subset)
    return powerset


def sum_up(S):
    total = 0
    for element in S:
        total += element
    return total


A = tuple(range(1, 13))
A_powerset = powerset(A)

T = int(input())
for test_case in range(1, T + 1):
    subset_len, subset_sum = map(int, input().split())
    matching = 0

    for subset in A_powerset:
        if len(subset) == subset_len and sum_up(subset) == subset_sum:
            matching += 1
    
    print("#{} {}".format(test_case, matching))
