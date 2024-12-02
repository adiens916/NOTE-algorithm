"""
어차피 노드에 들어오는 쪽이 전부 끝나야 함.
=> 들어오는 쪽 중 가장 늦게 끝나는 쪽이 기준이 될 수 밖에 없음.
"""
from collections import deque


# 입력
N = int(input())

graph: list[list[int]] = [[] for _ in range(N + 1)]
ins = [0] * (N + 1)
times = [0] * (N + 1)

for i in range(1, N + 1):
    info = list(map(int, input().split()))
    times[i] = info[0]
    for k in range(1, len(info) - 1):
        prev = info[k]
        graph[prev].append(i)
        ins[i] += 1

# 위상 정렬
queue = deque()
for v in range(1, N + 1):
    if ins[v] == 0:
        queue.append(v)

# DP 테이블
prev_maxes = [0] * (N + 1)
while queue:
    v = queue.popleft()
    # 이전까지의 선수 수업 중 가장 늦게 끝나는 수업의 시간을 더함.
    # 그래야 이 수업을 듣게 되었을 때까지의 시간을 알 수 있음.
    # 어차피 다음 수업들도 이 시간을 기준으로 하기에, 아예 값을 바꿔도 됨.
    times[v] += prev_maxes[v]

    for w in graph[v]:
        # 들어오는 쪽 중 가장 늦게 끝나는 쪽을 기준으로 함.
        prev_maxes[w] = max(prev_maxes[w], times[v])
        ins[w] -= 1
        if ins[w] == 0:
            queue.append(w)

# 결과
print(*times[1:], sep="\n")

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""