def find_parent(x: int, parents: list[int]) -> int:
    if x != parents[x]:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


def union(a: int, b: int, parents: list[int]) -> None:
    a = find_parent(a, parents)
    b = find_parent(b, parents)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


v, e = map(int, input().split())

graph = [i for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    union(a, b, graph)

print(graph[1:])
