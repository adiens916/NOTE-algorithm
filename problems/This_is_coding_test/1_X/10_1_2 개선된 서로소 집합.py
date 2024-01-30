def find_parent(x: int, parents: list[int]) -> int:
    if parents[x] == x:
        return x

    # 경로 압축
    parents[x] = find_parent(parents[x], parents)
    return parents[x]


def union_parent(a: int, b: int, parents: list[int]) -> None:
    A = find_parent(a, parents)
    B = find_parent(b, parents)

    if A < B:
        parents[B] = A
    else:
        parents[A] = B


V, E = map(int, input().split())
parents = [i for i in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    union_parent(a, b, parents)

print(parents)  # [0, 1, 1, 2, 1, 5, 5]


for i in range(1, V + 1):
    find_parent(i, parents)
# XXX: 모든 노드에 대해 한 번 더 부모 찾는 걸 실행해야 함.
# 자식 노드에 관한 정보가 없기에, 자식들을 역추적해서 갱신할 수 없기 때문.
# 만약 자식 노드 정보가 있다면, union 단계에서 갱신 가능.

# 그러나 효율적이라고는 할 수 없는 게, 매번 루트를 바꾸면 매번 갱신할 수도 있음...
# 예) 1 2, 3 4, 5 6, 7 8, {5 7, 3 5, 1 3}
# => 역시 지금처럼 한꺼번에 갱신하는 게 더 좋을 듯하다.

print(parents)  # [0, 1, 1, 1, 1, 5, 5]

"""
6 4
1 4
2 3
2 4
5 6
"""
