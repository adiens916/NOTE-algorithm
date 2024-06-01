N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

# XXX: 1e9는 실수라서 1,000,000,000.0 처럼 소수점이 붙음.
# 그래서 만약 최댓값이 10억이면, 갱신이 안 되므로 답에 소수점이 붙음...
# => int()를 씌우든지, 10억보다 크게 만들면 됨
# 출처: https://www.acmicpc.net/board/view/124742
max_value = int(-1e9)
min_value = int(1e9)


def calc_value_by_op(a: int, b: int, i: int) -> int:
    if i == 0:
        return a + b
    elif i == 1:
        return a - b
    elif i == 2:
        return a * b
    else:
        if a > 0:
            return a // b
        else:
            x = -a // b
            return -x


def dfs(index: int, value: int) -> None:
    global max_value
    global min_value

    if index == N - 1:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return

    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            new_value = calc_value_by_op(value, nums[index + 1], i)
            dfs(index + 1, new_value)
            ops[i] += 1


dfs(0, nums[0])
print(max_value)
print(min_value)

"""
2
5 6
0 0 1 0
"""  # 30 30
"""
3
3 4 5
1 0 1 0
"""  # 35 17
"""
6
1 2 3 4 5 6
2 1 1 1
"""  # 54 -24
