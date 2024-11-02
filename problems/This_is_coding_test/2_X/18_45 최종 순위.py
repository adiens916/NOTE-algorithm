from collections import deque


def make_graph(ranks):
    n = len(ranks)
    in_degrees = [0] * (n + 1)
    # 순서 바뀜 => 바꾸기 쉽게 인접 리스트 대신 인접 행렬 이용
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    # 1등팀부터 순서대로 출력 => 1등팀에서 다른 팀으로 들어가게 조정
    # XXX: 팀 개수는 N개니까, 범위도 N까지임.
    for i in range(n - 1):
        for j in range(i + 1, n):
            # XXX: 원래 팀 번호랑 순서랑 다름
            graph[ranks[i]][ranks[j]] = True
            in_degrees[ranks[j]] += 1

    return graph, in_degrees


def reverse_pair(graph, in_degrees, pairs):
    for a, b in pairs:
        if graph[a][b]:
            from_ = a
            to_ = b
        else:
            from_ = b
            to_ = a

        graph[from_][to_] = False
        graph[to_][from_] = True
        in_degrees[to_] -= 1
        in_degrees[from_] += 1


def topology_sort(graph, in_degrees):
    result = []
    n = len(graph) - 1

    queue = deque()
    for i in range(1, n + 1):
        if in_degrees[i] == 0:
            queue.append(i)

    # XXX: n번만 돌리기
    for i in range(1, n + 1):
        # XXX: 조건 먼저 체크 (쌍 바꾸는 과정에서 잘못 됐을 수도 있음.)
        if len(queue) == 0:
            return False, "IMPOSSIBLE"
        if len(queue) >= 2:
            return False, "?"

        a = queue.popleft()
        result.append(a)

        for b in range(1, n + 1):
            if graph[a][b]:
                in_degrees[b] -= 1
                if in_degrees[b] == 0:
                    queue.append(b)

    return True, result


T = int(input())
for _ in range(T):
    n = int(input())
    ranks = list(map(int, input().split()))
    m = int(input())
    pairs = [list(map(int, input().split())) for _ in range(m)]

    graph, in_degrees = make_graph(ranks)
    reverse_pair(graph, in_degrees, pairs)

    success, result = topology_sort(graph, in_degrees)
    if success:
        print(*result, sep=" ")
    else:
        print(result)
