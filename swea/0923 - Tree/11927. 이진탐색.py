from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
"이진 탐색 트리는 어떤 경우에도 저장된 값이 
왼쪽 서브트리의 루트 < 현재 노드 < 오른쪽 서브 트리의 루트"
순으로 값이 증가
-> L-V-R = 중위순회!
-> 중위순회 방식으로 채워넣기!
"""


def inorder(tree, i, N):
    global num

    # 자식 노드까지 = 트리 최대 범위까지
    if i <= N:
        inorder(tree, 2*i, N)
        tree[i] = num
        num += 1
        inorder(tree, 2*i + 1, N)
    

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    
    num = 1
    inorder(tree, 1, N)
    print('#{} {} {}'.format(test_case, tree[1], tree[N//2]))
