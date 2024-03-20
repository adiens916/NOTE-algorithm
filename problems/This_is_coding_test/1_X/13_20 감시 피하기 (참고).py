# 출처: https://www.acmicpc.net/source/54267600
# 조건 설정을 잘한 예시


import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())


def is_possible(S_list, T_list, O_list):
    for T in T_list:
        for S in S_list:
            # 선생과 학생이 같은 행 / 열에 있는 상황
            if T[0] == S[0] or T[1] == S[1]:
                a = 1
                for O in O_list:
                    # XXX: 같은 열에 있고 & 행이 순서대로 되어 있는 경우
                    # 혹은 같은 행에 있고 & 열이 순서대로 되어 있는 경우
                    if (T[1] == S[1] == O[1] and min(T[0], S[0]) < O[0] < max(T[0], S[0])) or \
                            (T[0] == S[0] == O[0] and min(T[1], S[1]) < O[1] < max(T[1], S[1])):
                        # 중간에 오는 장애물이 있으므로 감시 피함
                        a = 0
                        break
                # XXX: 같은 행 / 열에 있는 상황에서,
                # 만족하는 장애물이 하나도 없으므로, 초기 1 그대로 => False
                if a:
                    return 0
    return 1


S_list = []
T_list = []
can_O = []
for i in range(N):
    temp = input().rstrip().split()
    k = 0
    for s in temp:
        if s == 'X':
            can_O.append([i, k])
        elif s == 'T':
            T_list.append([i, k])
        else:
            S_list.append([i, k])
        k += 1

for O_list in combinations(can_O, 3):
    if is_possible(S_list, T_list, O_list):
        print('YES')
        exit()
print('NO')
