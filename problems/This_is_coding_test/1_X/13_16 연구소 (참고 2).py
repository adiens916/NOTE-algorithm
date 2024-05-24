# 굳이 deque 안 쓰고 stack으로도 가능
# https://www.acmicpc.net/source/19418408

from itertools import combinations

N, M = map(int, input().split())
org_box = [list(map(int, input().split())) for _ in range(N)]


def use_stack(N, M, org_box):
    space = [(n, m) for n in range(N) for m in range(M) if not org_box[n][m]]
    virus = [(n, m) for n in range(N) for m in range(M) if org_box[n][m] == 2]
    S = len(space)

    result = -1

    for pair in combinations(range(S), 3):
        box = [b[:] for b in org_box]
        for d in pair:
            y, x = space[d]
            box[y][x] = 1
        stack = [(n, m) for n, m in virus]
        count = S - 3
        while stack:
            y, x = stack.pop()
            if count < result: break
            for n, m in (0, 1), (-1, 0), (0, -1), (1, 0):
                if 0 <= y + n < N and 0 <= x + m < M and not box[y + n][x + m]:
                    box[y + n][x + m] = 2
                    count -= 1
                    stack.append((y + n, x + m))
        result = max(result, count)
    return result


print(use_stack(N, M, org_box))
