import sys
input = sys.stdin.readline

# 최소 신장 트리 = 최소 힙 + 서로소 알고리즘
import heapq


def find_parent(x, parents):
    if parents[x] != x:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


N = int(input())
# XXX: 정렬해야 하므로, 원래 인덱스도 같이 보존.
planets = [list(map(int, input().split())) + [i] for i in range(N)]

# XXX: N^2 하면 1e10이 되므로, 시간 초과임.
# => 각 '축' 별로 인접 경로 모아서 만들기 (1차원 * 3개의 축)
# 참고: https://www.acmicpc.net/board/view/145011
tunnels = []
for axis in range(3):
    s_planets = sorted(planets, key=lambda p: p[axis])
    for k in range(N - 1):
        a = s_planets[k]
        b = s_planets[k + 1]
        tunnel = b[axis] - a[axis]
        tunnels.append((tunnel, a[3], b[3]))

parents = [i for i in range(N)]
min_sum = 0

heapq.heapify(tunnels)
while tunnels:
    tunnel, a, b = heapq.heappop(tunnels)

    pa = find_parent(a, parents)
    pb = find_parent(b, parents)

    if pa != pb:
        min_sum += tunnel
        if pa < pb:
            # XXX: 끝 조상을 다른 쪽으로 연결시켜야 함.
            parents[pb] = pa
        else:
            parents[pa] = pb

print(min_sum)

"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""  # 4

"""
6
0 0 0
1 1 1
-5 -5 -5
-6 -6 170
-1 -1 170
-4 -4 172
"""  # 4

