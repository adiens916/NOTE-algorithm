from os import read
from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def is_pair_parenthese(string):
    parentheses = (("(", ")"), ("{", "}"))
    stack = []

    for char in string:
        for i in range(len(parentheses)):
            if char == parentheses[i][0]:
                # 괄호 대신에 괄호 인덱스를 push
                stack.append(i)

            elif char == parentheses[i][1]:
                # FIXME: 스택 안에 열린 괄호가 없는 경우도 체크
                if len(stack) == 0:
                    return False

                paren_idx = stack[-1]
                # 괄호 인덱스가 같다면 같은 괄호
                # -> 맨 위에 있는 것 pop
                if paren_idx == i:
                    stack.pop()
                else:
                    return False
            else:
                continue
    
    # 괄호가 짝이 맞아 전부 사라졌다면 스택이 비어야 함
    if len(stack) == 0:
        return True
    else:
        return False


T = int(input())
for test_case in range(1, T + 1):
    string = input()
    result = int(is_pair_parenthese(string))
    print("#{} {}".format(test_case, result))
