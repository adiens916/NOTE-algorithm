# 출처: https://www.acmicpc.net/source/71543540
# 메모이제이션 기법을 활용해서, 같은 조합일 때의 크기를 빠르게 계산

def operate(o1, o2, o3, o4, x, k):  # brute force
    if k == N:  # 0 0 0 0
        return
    y = arr[k]
    if o1: dfs(o1 - 1, o2, o3, o4, x + y, k + 1)
    if o2: dfs(o1, o2 - 1, o3, o4, x - y, k + 1)
    if o3: dfs(o1, o2, o3 - 1, o4, x * y, k + 1)
    if o4: dfs(o1, o2, o3, o4 - 1, x // y if x >= 0 else -(-(x) // y), k + 1)


def dfs(o1, o2, o3, o4, x, k):
    if (o1, o2, o3, o4) in memo_max:  # maximum value memoization
        if x > memo_max[(o1, o2, o3, o4)]:
            memo_max[(o1, o2, o3, o4)] = x
            operate(o1, o2, o3, o4, x, k)
    else:
        memo_max[(o1, o2, o3, o4)] = x
        operate(o1, o2, o3, o4, x, k)

    if (o1, o2, o3, o4) in memo_min:  # minimum value memoization
        if x < memo_min[(o1, o2, o3, o4)]:
            memo_min[(o1, o2, o3, o4)] = x
            operate(o1, o2, o3, o4, x, k)
    else:
        memo_min[(o1, o2, o3, o4)] = x
        operate(o1, o2, o3, o4, x, k)


N = int(input())
arr = [*map(int, input().split())]
oper = tuple(map(int, input().split()))
memo_max = {}
memo_min = {}

dfs(*oper, arr[0], 1)
print(memo_max[(0, 0, 0, 0)])
print(memo_min[(0, 0, 0, 0)])