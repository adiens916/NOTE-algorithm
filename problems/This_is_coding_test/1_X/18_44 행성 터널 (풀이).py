# 우선순위 큐를 이용해서 풀면 1400 밀리초가 걸리는데,
# 이 방식으로 풀면 876 밀리초가 나옴.
# 아마 우선순위 큐는 매번 집어넣을 때 O(logN)만큼 걸리고,
# 정렬은 집어넣을 때 O(1)에 나중에 한꺼번에 O(NlogN)로 정렬해서 그런 듯?...
# https://www.acmicpc.net/source/74392611

import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution():
    N = int(input())
    nodes = []
    for i in range(N):
        X, Y, Z = map(int, input().split())
        nodes.append((i + 1, X, Y, Z))

    # 1. x, y, z 축으로 정렬하여 이웃한 행성들의 edges 를 얻는다.
    edges = []
    # 1-1 dim축 기준으로 정렬 후 인접한 행성 edges에 추가
    for dim in range(1, 4):  # 1:x, 2:y, 3:z
        sorted_list = sorted(nodes, key=lambda x: x[dim])
        for i in range(N - 1):
            cost = abs(sorted_list[i][dim] - sorted_list[i + 1][dim])
            v1 = sorted_list[i][0]
            v2 = sorted_list[i + 1][0]
            edges.append((cost, v1, v2))

    # 2. 얻은 edges를 기반으로 크루스칼 알고리즘을 수행한다.
    parent = [i for i in range(N + 1)]
    answer = 0
    for edge in sorted(edges):
        w, v1, v2 = edge

        # 2-1. v1, v2의 루트 노드가 다른 경우에만 Union 작업 실행
        if find_parent(parent, v1) != find_parent(parent, v2):
            union_parent(parent, v1, v2)
            answer += w
    return answer


if __name__ == "__main__":
    answer = solution()
    print(answer)
