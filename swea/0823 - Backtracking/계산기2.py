from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


priority = {'+': 1, '*': 2}


def to_postfix(exp):
    # 괄호가 없는 경우의 계산
    op_stack = []
    result = []

    for char in exp:
        if '0' <= char <= '9':
            result.append(char)
        else:
            if not op_stack:
                op_stack.append(char)
            elif priority[char] > priority[op_stack[-1]]:
                op_stack.append(char)
            else:
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
