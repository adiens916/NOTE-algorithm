N = int(input())

max_cases = [0] * (N + 1)
max_cases[1] = 1
max_cases[2] = 3

for i in range(3, N + 1):
    # XXX: 오로지 이전 항들만 생각하기.
    # 맨 처음이 어떤지는 신경쓰지 않음.

    # XXX: 2를 더하는 게 아니라 곱하는 이유는,
    # 아예 다른 경우가 되기 때문에 가지쳐서 나가기 떄문.
    max_cases[i] = max_cases[i - 1] + max_cases[i - 2] * 2

print(max_cases[N])

"""
3
"""
