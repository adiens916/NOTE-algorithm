def find_parent(x: int, parents: list[int]) -> int:
    if parents[x] != x:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


def union(a: int, b: int, parents: list[int]) -> None:
    ap = find_parent(a, parents)
    bp = find_parent(b, parents)

    if ap < bp:
        parents[b] = ap
    else:
        parents[a] = bp


V, E = map(int, input().split())
parents = [i for i in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    union(a, b, parents)

print(parents[1:])

"""
6 4
1 4
2 3
2 4
5 6
"""
