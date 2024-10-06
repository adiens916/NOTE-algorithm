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
        # XXX: for 문으로 하면 안 됨.
        # for 문에 들어간 범위 값은 고정되므로, 무조건 해당 값만큼 반복.
        # 그래서 실제보다 더 많이 반복해서 계산하게 됨 (중복)
        # => 실제 값 참조하는 리스트 & if 문 이용해야 함.
        for _ in range(add):
            add -= 1
            permutation(k + 1, cur_num + nums[k + 1])
            add += 1
        for _ in range(sub):
            sub -= 1
            permutation(k + 1, cur_num - nums[k + 1])
            sub += 1
        for _ in range(mul):
            mul -= 1
            permutation(k + 1, cur_num * nums[k + 1])
            mul += 1
        for _ in range(div):
            if cur_num < 0:
                next_num = -(-cur_num // nums[k + 1])
            else:
                next_num = cur_num // nums[k + 1]
            div -= 1
            # XXX: 원본 값을 내려 보내지 말고, 복사본을 수정해서 전달하기
            # 그러면 원본 값을 다시 복구하느라, 필요없는 연산을 안 해도 됨.
            permutation(k + 1, next_num)
            div += 1


permutation(0, nums[0])
print(max_val)
print(min_val)
