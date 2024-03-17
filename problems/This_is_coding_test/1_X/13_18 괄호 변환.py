def solution(p: str) -> str:
    answer = fix(p)
    return answer


def fix(s: str) -> str:
    # XXX: 빈 문자열이면 빈 문자열 반환
    if s == "":
        return ""

    u, v, is_u_right = partition(s)
    if is_u_right:
        return u + fix(v)
    else:
        return "(" + fix(v) + ")" + reverse_p(u)[1:-2]


def partition(s: str) -> tuple:
    stack = 0
    left = 0
    right = 0

    for i in range(len(s)):
        if s[i] == "(":
            left += 1
            stack += 1
        else:
            right += 1
            # XXX: 스택이 (가 채워져 있는 경우에만
            if stack > 0:
                # 쌍 이뤄서 제거하고 스택 감소
                stack -= 1

        if left == right:
            u = s[: i + 1]
            v = s[i + 1 :]
            # 스택이 빈 경우면 올바른 문자열임
            is_right = stack == 0
            return u, v, is_right


def reverse_p(s: str) -> str:
    # XXX: 문자열을 뒤집는 게 아니라, 괄호를 뒤집어야 함
    # 예) ))(()( 주어진 경우,
    # 문자열을 뒤집으면 ()(())
    # 괄호를 뒤집으면 (())()
    r = []
    for c in s:
        if c == "(":
            r.append(")")
        else:
            r.append("(")
    return "".join(r)


"""
()))((()
# ()(())()
"""
"""
(()())()
# (()())()
"""
