from pathlib import Path
from typing import Tuple
directory = Path(__file__).parent
file_name = Path(__file__).stem
input_text = rf"{directory}\{file_name}_input.txt"

import sys
sys.stdin = open(input_text)
input = sys.stdin.readline

##################################################
def fix(string: str) -> str:
    if string == '':
        return ''

    u, v = split_parentheses(string)
    if is_right_parentheses(u):
        return u + fix(v)
    else:
        return '(' + fix(v) + ')' + inner_reverse(u)


def split_parentheses(string: str) -> Tuple[str, str]:
    count_left = 0
    count_right = 0

    for i in range(len(string)):
        if string[i] == '(':
            count_left += 1
        elif string[i] == ')':
            count_right += 1
        
        if count_left == count_right:
            return string[0: i+1], string[i+1: ]


def is_right_parentheses(string: str) -> bool:
    bin_stack = []
    for parenthesis in string:
        # 삭제하기 위한 모든 조건 체크
        # 스택 참고하기 전에 있는지부터 체크
        if bin_stack and bin_stack[-1] == '(' and parenthesis == ')':
            bin_stack.pop()
        # 조건에 안 맞으면 넣기
        else:
            bin_stack.append(parenthesis)
    
    if bin_stack == []:
        return True
    else:
        return False


def inner_reverse(string: str) -> str:
    return string[-2: 0: -1]


# def test_split():
#     string = '()))(('
#     u, v = split_parentheses(string)
#     assert u == '()'
#     assert v == '))(('


# def test_is_right_parentheses():
#     assert is_right_parentheses('(()())') == True


# def test_inner_reverse():
#     assert reverse_inner('12345') == '432'
#     assert reverse_inner('()') == ''
#     assert reverse_inner('(())') == ')('


def test():
    # assert fix('()') == '()'
    # assert fix(')(') == '()'
    # assert fix('()()') == '()()'
    # assert fix('(()())') == '(()())'
    # assert fix('()(()())') == '()(()())'
    assert fix(')(()') == '(())'
    assert fix(')()(') == '(())'
    assert fix(')()(()') == '((()))'
    assert fix(')()(()()') == '((()()))'


if __name__ == '__main__':
    string = input().strip()
    print(fix(string))