def find_parent(x: int, parents: list[int]) -> int:
    if parents[x] != x:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


def union_parent(a: int, b: int, parents: list[int]) -> None:
    a = find_parent(a, parents)
    b = find_parent(b, parents)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


V, E = map(int, input().split())
parents = [i for i in range(V + 1)]

is_cyclic = False
for _ in range(E):
    a, b = map(int, input().split())

    # 달라지는 부분
    A = find_parent(a, parents)
    B = find_parent(b, parents)

    if A == B:
        is_cyclic = True
        break
    else:
        union_parent(A, B, parents)

if is_cyclic:
    print("cyclic")
else:
    print("acyclic")

"""
3 3
2 3
1 2
1 3
"""
