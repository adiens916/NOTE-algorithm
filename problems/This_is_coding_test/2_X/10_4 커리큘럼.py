# 참고: https://imhihi.tistory.com/entry/이코테-09-그래프-이론-커리큘럼
from collections import deque

N = int(input())

nodes = [0] * (N + 1)
# XXX: 다음 노드로 가는 배열은 필수. 그래야 in_degree 체크 가능.
graph: list[list[int]] = [[] for _ in range(N + 1)]
in_degrees = [0] * (N + 1)
queue = deque()

for i in range(1, N + 1):
    lec_info = list(map(int, input().split()))
    lec_time, *prev_list, _ = lec_info

    nodes[i] = lec_time
    for prev in prev_list:
        # 이전 노드로 가는 건 필요 없음.
        graph[prev].append(i)
        in_degrees[i] += 1
    if len(prev_list) == 0:
        queue.append(i)

# XXX: 값 저장할 배열 초기화
table = [t for t in nodes]
# 위상 정렬
while queue:
    start = queue.popleft()

    for next_ in graph[start]:
        # XXX: 항상 체크하면서 더 큰 값을 저장 (DP)
        table[next_] = max(table[next_], table[start] + nodes[next_])

        in_degrees[next_] -= 1
        if in_degrees[next_] == 0:
            queue.append(next_)

print(*nodes[1:], sep='\n')

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
"""  # 답
10
20
14
18
17
"""
