import sys
sys.stdin = open("이진탐색_input.txt")
def inorder(v):
    global idx
    if v <= N:
        inorder(v * 2) #왼쪽자식
        tree[v] = idx
        idx += 1
        inorder(v * 2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    idx = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
