from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
# input = sys.stdin.readline


def calc(exp):
    stack = []

    for char in exp:
        if '0' <= char <= '9':
            stack.append(int(char))
        else:
            # 마지막 도착하면 종료
            if char == '.':
                break

            # 두 개 이상 없으면 연산 불가
            if len(stack) < 2:
                return 'error'
            b = stack.pop()
            a = stack.pop()

            result = 0
            if char == '+':
                result = a + b
            elif char == '-':
                result = a - b
            elif char == '*':
                result = a * b
            elif char == '/':
                result = a // b
            stack.append(result)

    # 숫자가 딱 한 개 남아 있어야 정상
    if len(stack) == 1:
        return stack[0]
    # 스택 안에 숫자가 여러 개 들어있는 경우는 에러
    else:
        return 'error'


T = int(input())
for test_case in range(1, T + 1):
    exp = input().split()
    result = calc(exp)
    print("#{} {}".format(test_case, result))

"""
출력
#1 84
#2 error
#3 168
"""