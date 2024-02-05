from collections import deque

V = int(input())

times = [0] * (V + 1)
in_degrees = [0] * (V + 1)
graph = [[] for _ in range(V + 1)]

for i in range(1, V + 1):
    data = list(map(int, input().split()))
    times[i] = data[0]
    for prev in data[1:-1]:
        # XXX: x 대신에 prev 같은 명칭을 써야 순서가 안 헷갈림
        graph[prev].append(i)
        in_degrees[i] += 1


def topology_sort() -> list[int]:
    max_times = [0] * (V + 1)
    queue = deque()

    # 진입차수 0 찾아 넣기
    for i in range(1, V + 1):
        if in_degrees[i] == 0:
            queue.append(i)
            # XXX: 진입차수가 0인 애들은 최댓값 비교가 이루어지지 않음
            # => 맨 처음부터 자기 자신으로 초기화 필요
            max_times[i] = times[i]

    while any(queue):
        now = queue.popleft()

        for next in graph[now]:
            max_times[next] = max(max_times[next], max_times[now] + times[next])
            in_degrees[next] -= 1
            if in_degrees[next] == 0:
                queue.append(next)

    return max_times


max_times = topology_sort()
print(*max_times[1:], sep="\n")

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""  # 10 20 14 18 17
