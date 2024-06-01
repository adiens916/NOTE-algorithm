# 최대 금액 = 전체 - 최소 길이
# 최소 길이 = 최소 신장 트리
# => 크루스칼 알고리즘 = 우선순위 큐 + 서로소 알고리즘
import heapq


def find_parent(x: int, parents: list[int]) -> int:
    if parents[x] != x:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


def union(a: int, b: int, parents: list[int]) -> None:
    a = find_parent(a, parents)
    b = find_parent(b, parents)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N, M = map(int, input().split())

# 거리가 작은 순서대로 우선순위 큐에 넣기
# 이때 전체 거리 계산
queue = []
total_cost = 0
for _ in range(M):
    X, Y, Z = map(int, input().split())
    heapq.heappush(queue, (Z, X, Y))
    total_cost += Z

# 서로소 알고리즘을 위한 준비
parents = [i for i in range(N)]
min_cost = 0

while queue:
    # 선분 하나 꺼냄
    cost, x, y = heapq.heappop(queue)

    # 두 정점의 루트 노드 찾기
    x_root = find_parent(x, parents)
    y_root = find_parent(y, parents)

    # 두 정점의 루트 노드가 같으면 = 이미 더 작은 선분이 그래프에 포함되어 있음.
    if x_root == y_root:
        # 추가하지 않고 스킵 (추가하면 사이클 생김)
        continue
    # 포함되어 있지 않으면
    else:
        # 두 정점 그룹을 합침
        union(x_root, y_root, parents)
        # 해당 선분 길이 추가
        min_cost += cost

print(total_cost - min_cost)

"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""  # 51
