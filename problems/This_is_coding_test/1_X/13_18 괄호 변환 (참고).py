# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/60058/solution_groups?language=python3


def solution(p):
    # 1
    if p == "":
        return p

    # 2
    is_right_brck = True
    c = 0
    for i in range(len(p)):
        if p[i] == "(":
            c -= 1
        else:
            c += 1

        # XXX: left, right 변수 안 쓰고 stack만 가지고도 올바름 판별 가능
        # '('이면 stack ++, ')'이면 stack --
        # stack이 음수가 된 적이 한 번이라도 있으면 매칭 X
        # stack이 0이 되면 좌우 개수 같음
        if c > 0:
            is_right_brck = False
        if c == 0:
            if is_right_brck:
                return p[: i + 1] + solution(p[i + 1 :])
            else:
                return (
                    "("
                    + solution(p[i + 1 :])
                    + ")"
                    + "".join(list(map(lambda x: "(" if x == ")" else ")", p[1:i])))
                )
