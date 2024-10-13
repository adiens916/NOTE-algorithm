def find_parent(x: int, parents: list[int]) -> int:
    if x != parents[x]:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


G = int(input())
P = int(input())
plights = [int(input()) for _ in range(P)]

# XXX: 서로소 알고리즘 이용. 번호가 겹칠 때마다 루트를 1씩 줄여 나가기.
parents = [i for i in range(G + 1)]

for i in range(P):
    gi = plights[i]
    root = find_parent(gi, parents)

    if root == 0:
        print(i)
        break
    else:
        # union 할 필요없이, 루트를 1만 줄여도 됨.
        # 어차피 다음 번에 루트 찾는 과정에서, 이어서 찾게 됨.
        parents[root] -= 1
