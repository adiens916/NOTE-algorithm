N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
plans = list(map(int, input().split()))

# 도시들이 서로 연결되어 있는지만 알면 됨
# => 서로소 알고리즘 이용
roots = [i for i in range(N + 1)]


def find(x: int, roots: list[int]) -> int:
    if x != roots[x]:
        roots[x] = find(roots[x], roots)
    return roots[x]


def union(a: int, b: int, roots: list[int]) -> None:
    a = find(a, roots)
    b = find(b, roots)
    if a < b:
        roots[b] = a
    else:
        roots[a] = b


# 각 도시들이 연결된 경우, 루트 번호 일치시키기
for y in range(N):
    for x in range(N):
        if arr[y][x] == 1:
            union(y + 1, x + 1, roots)

# 여행 게획들 순회 하면서, 루트 번호 다른 게 있나 확인
group_root = find(plans[0] + 1, roots)
for city in plans:
    if group_root != find(city, roots):
        print("NO")
        exit()
print("YES")

"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""  # YES
