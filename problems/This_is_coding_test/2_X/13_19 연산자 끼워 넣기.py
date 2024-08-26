"""
수의 순서 바꾸면 안됨
앞에서부터 진행
정수 나눗셈으로 몫만
음수 나눗셈은 양수로 바꾼 뒤 몫 취하고, 그 몫을 음수로
결과 최대와 최소 구하기
"""

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -int(1e9)
min_val = int(1e9)


def permutation(k, cur_num):
    global max_val
    global min_val
    global add
    global sub
    global mul
    global div

    if k == N - 1:
        max_val = max(max_val, cur_num)
        min_val = min(min_val, cur_num)
        return
    else:
        for _ in range(add):
            cur_num += nums[k + 1]
            add -= 1
            permutation(k + 1, cur_num)
            add += 1
            cur_num -= nums[k + 1]
        for _ in range(sub):
            cur_num -= nums[k + 1]
            sub -= 1
            permutation(k + 1, cur_num)
            sub += 1
            cur_num += nums[k + 1]
        for _ in range(mul):
            cur_num *= nums[k + 1]
            mul -= 1
            permutation(k + 1, cur_num)
            mul += 1
            cur_num //= nums[k + 1]
        for _ in range(div):
            origin = cur_num
            if cur_num < 0:
                cur_num = -(-cur_num // nums[k + 1])
            else:
                cur_num //= nums[k + 1]
            div -= 1
            permutation(k + 1, cur_num)
            div += 1
            # XXX: 나눗셈의 몫만 취했으므로, 그대로 곱하면 나머지가 손실됨. 원본 값 보존 필요.
            cur_num = origin


permutation(0, nums[0])
print(max_val)
print(min_val)
