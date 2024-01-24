# XXX: N 크기를 꼭 지정해줘야 함 / 그래프에서 비어있는 모든 노드를 포함해야 함
# 값이 들어있는 노드만으로 그래프를 구성하는 경우, 인덱스 모자라서 IndexError 발생.
graph = [
    [],
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    [],
]
N = 6

INF = int(1e9)
min_lengths = [INF] * (N + 1)
visited = [False] * (N + 1)


# XXX: 선택 정렬의 응용
def get_node_of_min_length() -> int:
    min_value = INF
    min_index = 0

    for i in range(1, N + 1):
        if not visited[i] and min_lengths[i] < min_value:
            min_value = min_lengths[i]
            min_index = i

    return min_index


# XXX: BFS와 형태가 유사
def dijkstra_simple(start: int) -> list[int]:
    min_lengths[start] = 0

    # 마지막은 한 개만 남으므로, N - 1개만 해도 됨.
    for _ in range(N - 1):
        start = get_node_of_min_length()
        visited[start] = True

        for dest, edge in graph[start]:
            cost = min_lengths[start] + edge
            if cost < min_lengths[dest]:
                min_lengths[dest] = cost

    return min_lengths


min_lengths = dijkstra_simple(1)
print(min_lengths[1:])
