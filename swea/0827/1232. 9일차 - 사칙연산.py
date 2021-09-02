from pathlib import Path
import sys
from typing import List

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
# input = sys.stdin.readline


class Node:
    # 자식이 없는 경우 초기값을 0으로 설정
    def __init__(self, val=0, left=0, right=0) -> None:
        self.val = val
        self.left = left
        self.right = right


def calc(node=1):
    global tree

    # 노드의 값
    op = tree[node].val
    # 숫자면 바로 반환
    if isinstance(op, int):
        return op

    # 원래는 if로 자식 노드가 있을 때만 참고해야 함.
    # 그런데 조건에서 연산자는 무조건 자식 노드가 있음.
    # -> 따라서 if 안 쓰고 그냥 참고해도 무방.
    left = calc(tree[node].left)
    right = calc(tree[node].right)

    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    elif op == "*":
        return left * right
    elif op == "/":
        return left / right


T = 10
for test_case in range(1, T + 1):
    N = int(input())
    tree = [Node() for _ in range(N + 1)]

    # 정점 정보 입력
    for _ in range(N):
        node, *node_info = input().split()
        node = int(node)

        # 연산자가 아닌 경우
        if node_info[0].isdecimal():
            tree[node].val = int(node_info[0])
        # 연산자인 경우
        else:
            tree[node].val = node_info[0]
            tree[node].left = int(node_info[1])
            tree[node].right = int(node_info[2])
    
    # 후위 순회로 계산
    result = calc()
    print("#{} {}".format(test_case, int(result)))
