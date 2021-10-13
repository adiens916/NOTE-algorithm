import sys
sys.stdin = open("subtree_input.txt")

def preorder(node):
    global cnt
    if node != 0:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())  # 간선수, 서브트리의 루트노드
    tree = [[0] * 3 for _ in range(E+2)] # left, right, parent
    temp = list(map(int, input().split()))
    for i in range(E):
        p = temp[i*2]
        c = temp[i*2 + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p

    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')