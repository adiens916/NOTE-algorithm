# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=449&sca=2080

def nTTr(n, r, k):
    if k == r:
        print(*case)
    else:
        for i in range(1, n + 1):
            case[k] = i
            nTTr(n, r, k + 1)


def nHr(n, r, k, start):
    if k == r:
        print(*case)
    else:
        for i in range(start, n + 1):
            case[k] = i
            nHr(n, r, k + 1, i)


def nPr(n, r, k):
    if k == r:
        print(*case)
    else:
        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                case[k] = i
                nPr(n, r, k + 1)
                used[i] = False


N, M = map(int, input().split())
case = [0] * N
used = [False] * 7

if M == 1:
    nTTr(6, N, 0)
elif M == 2:
    nHr(6, N, 0, 1)
elif M == 3:
    nPr(6, N, 0)
