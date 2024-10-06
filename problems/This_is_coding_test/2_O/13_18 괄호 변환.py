"""
균형잡힘으로 분리
u 올바름 -> v 수정 후, u에 이어 붙여서 반환
u 안 올바름 -> 나머지 문자열 괄호 방향 뒤집어서 붙이기
! 역으로 읽는 게 아니라, 각 괄호 검사 필요
"""


def solution(p):
    answer = convert(p)
    return answer


def convert(w: str) -> str:
    if w == "":
        return ""

    u, v = separate(w)
    if is_proper(u):
        return u + convert(v)
    else:
        front = "(" + convert(v) + ")"
        back = mirror(u)
        return front + back


def separate(w: str):
    stack = 0
    for i in range(len(w)):
        if w[i] == "(":
            stack -= 1
        else:
            stack += 1

        if stack == 0:
            return w[:i + 1], w[i + 1:]
    return w, ""


def is_proper(u: str) -> bool:
    stack = 0
    for i in range(len(u)):
        if u[i] == "(":
            stack -= 1
        else:
            stack += 1

        if stack > 0:
            return False
    return True


def mirror(s: str) -> str:
    result = []
    for i in range(1, len(s) - 1):
        if s[i] == "(":
            result.append(")")
        else:
            result.append("(")
    return ''.join(result)
