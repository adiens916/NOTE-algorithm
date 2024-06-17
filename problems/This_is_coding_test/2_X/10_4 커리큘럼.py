from collections import deque


N = int(input())

nodes = [0] * (N + 1)
next_nodes = [[] for _ in range(N + 1)]
prev_nodes = [[] for _ in range(N + 1)]
in_degrees = [0] * (N + 1)
queue = deque()

for i in range(1, N + 1):
    lec_info = list(map(int, input().split()))
    lec_time, *prev_list, _ = lec_info

    nodes[i] = lec_time
    for v in prev_list:
        prev_nodes[i].append(v)
        next_nodes[v].append(i)
        in_degrees[i] += 1
    if len(prev_list) == 0:
        queue.append(i)


while queue:
    node = queue.popleft()

    for v in next_nodes[node]:
        in_degrees[v] -= 1
        if in_degrees[v] == 0:
            prev_max = max([nodes[i] for i in prev_nodes[v]])
            nodes[v] += prev_max
            queue.append(v)


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
