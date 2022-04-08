import sys
sys.stdin = open("사칙연산_input.txt", "r")


def calc(op, left, right):
    if op == '+':
        result = left + right
    elif op == '-':
        result = left - right
    elif op == '*':
        result = left * right
    elif op == '/':
        result = left / right

    return result

T = 10
for tc in range(T):
    N = int(input())
    stack=[]
    oper = [''] * (N+1)
    firstChild  = [0] * (N+1)
    secondChild = [0] * (N+1)
    num = [0] *(N+1)
    for i in range(N):  # 입력
        temp = list(input().split())
        no = int(temp[0])
        if temp[1] == '+' or temp[1] == '-' or temp[1] == '*' or temp[1] == '/':
            oper[no] = temp[1]
            firstChild[no] = int(temp[2])
            secondChild[no] = int(temp[3])
            stack.append(no)
        else:
            num[no] = int(temp[1])

    while len(stack) != 0:  #스택 이용해서 연산자를 숫자로 계산
        idx = stack.pop()
        num[idx] = calc(oper[idx], num[firstChild[idx]], num[secondChild[idx]])

    print(f"#{tc+1} {int(num[1])}")