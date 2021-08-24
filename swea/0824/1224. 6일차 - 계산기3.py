from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
# input = sys.stdin.readline


# 괄호가 있는 경우의 계산
priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}


def to_postfix(exp):
    op_stack = []
    result = []

    for char in exp:
        if '0' <= char <= '9':
            result.append(char)
        else:
            # 여는 괄호인 경우 무조건 집어넣기
            if char == '(':
                op_stack.append(char)
            elif char == ')':
                # 여는 괄호가 나올 때까지 훑음
                while op_stack[-1] != '(':
                    result.append(op_stack.pop())
                op_stack.pop()

            # 우선순위가 높으면 나중에 처리
            elif priority[char] > priority[op_stack[-1]]:
                op_stack.append(char)
            # 우선순위가 낮거나 같은 경우
            else:
                # 앞쪽의 우선순위가 높은 것들을 먼저 처리
                while priority[char] <= priority[op_stack[-1]]:
                    result.append(op_stack.pop())
                    if not op_stack:
                        break
                op_stack.append(char)

    while op_stack:
        result.append(op_stack.pop())

    return result


def calc(exp2):
    stack = []

    for char in exp2:
        if '0' <= char <= '9':
            stack.append(int(char))
        else:
            if char == '+':
                result = stack.pop() + stack.pop()
            elif char == "*":
                result = stack.pop() * stack.pop()
            stack.append(result)

    return stack[0]


T = 10
for test_case in range(1, T + 1):
    input()
    exp = input().rstrip()
    exp2 = to_postfix(exp)
    result = calc(exp2)
    print('#{} {}'.format(test_case, result))
