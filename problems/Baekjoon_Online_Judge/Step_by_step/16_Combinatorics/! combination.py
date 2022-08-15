def nCr(n, r, k, start):
    """
    n: 전체 범위
    r: 뽑아야 하는 개수
    k: 현재까지 뽑은 개수
    start: 시작 범위
    """
    if k == r:
        print(*case)
    else:
        for i in range(start, n):
            case[k] = i
            nCr(n, r, k + 1, i + 1)


N = 5
M = 3
case = [0] * M
nCr(N, M, 0, 0)
print()

"""
1 2 3
1 2 4
1 2 5
1 3 4
1 3 5
1 4 5
2 3 4
2 3 5
2 4 5
3 4 5
"""


def nCr_desc(n, r):
    """
    n: 선택 가능한 숫자 중 최대
    r: 선택된 숫자가 들어갈 위치
    """
    if r == 0:              # 끝까지 간 경우 O
        print(*case)
    elif n < r:             # 위치가 더 작아지면 X
        return
    else:
        case[r - 1] = n - 1      # 끝자리에 넣기
        nCr_desc(n - 1, r - 1)  # 선택하고 다음 것
        nCr_desc(n - 1, r)      # 선택 안 하고 다음 것


N = 5
M = 3
case = [0] * M
nCr_desc(N, M)
print()


"""
3 4 5
2 4 5
1 4 5
2 3 5
1 3 5
1 2 5
2 3 4
1 3 4
1 2 4
1 2 3
"""


def nHr(n, r, k, start):
    """
    중복조합 = 조합 + 이전 값도 포함 가능
    """
    if k == r:
        print(*case)
    else:
        for i in range(start, n):
            case[k] = i
            nHr(n, r, k + 1, i)     # 이전 값도 중복 가능


N = 5
M = 3
case = [0] * M
nHr(N, M, 0, 0)
print()
