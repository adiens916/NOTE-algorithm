def find_parent(parents: list[int], x: int) -> int:
    if parents[x] == x:
        return x

    return find_parent(parents, parents[x])


def union_parent(parents: list[int], a: int, b: int) -> None:
    A = find_parent(parents, a)
    B = find_parent(parents, b)

    if A < B:
        parents[B] = A
    else:
        parents[A] = B


# 입력
v, e = map(int, input().split())

# 초기화
parents = [i for i in range(v + 1)]

# union 연산 수행
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parents, a, b)


# 출력 (간접 부모)
print(f"\n그룹: ", end="")
for i in range(1, v + 1):
    print(find_parent(parents, i), end=" ")

# 출력 (직접 부모)
print(f"\n직접적인 부모: ", end="")
for i in range(1, v + 1):
    print(parents[i], end=" ")

"""
6 4
1 4
2 3
2 4
5 6
"""
# 1 1 1 1 5 5
# 1 1 2 1 5 5
