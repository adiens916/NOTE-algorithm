from collections import deque


V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
in_degrees = [0] * (V + 1)

for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degrees[B] += 1


def topology_sort() -> list[int]:
    sort_result = []

    queue = deque()

    # XXX: 처음 진입 차수가 0인 걸 찾을 때는 정렬 없이도 가능.
    # 아니, 사실상 이게 O(N)으로 제일 빠르긴 함.
    for i in range(1, V + 1):
        if in_degrees[i] == 0:
            queue.append(i)

    while queue:
        start = queue.popleft()

        sort_result.append(start)

        for next in graph[start]:
            in_degrees[next] -= 1
            # XXX: 0일 때만 넣기
            # 만약 진입차수가 여러 개여도, 어차피 마지막 진입차수에서는 0이 됨.
            # 마이너스로 내려가거나 할 일은 없음.
            if in_degrees[next] == 0:
                queue.append(next)

    return sort_result


print(topology_sort())

"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
