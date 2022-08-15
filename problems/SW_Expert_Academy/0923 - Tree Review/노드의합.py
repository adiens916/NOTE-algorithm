import sys
sys.stdin = open('노드의합_input.txt')
def post_order(node):
    # 유효한 노드 인지 검사 node와 N 비교
    if node > N :
        return 0
    else:   # 유효한 노드
        # 잎노드
        if tree[node] != 0:
            return tree[node]
        # 가지노드
        else:
            left = post_order(2 * node)    # 왼쪽으로 이동
            right = post_order(2 * node + 1) # 오른쪽 이동
            tree[node] = left + right        # 양쪽값 더해서 저장
            return tree[node]             # 노드 저장된 값 반환



T = int(input())
for tc in range(1, T+1):
    # 노드수, 립노드수, 출력노드
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for i in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value
    post_order(1)
    print(f'#{tc} {tree[L]}')