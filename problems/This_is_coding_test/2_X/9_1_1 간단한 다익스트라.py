INF = int(1e9)


def find_shortest_node(table: list[int], visited: list[bool]) -> int:
    # XXX: 간단한 다익스트라에선 큐를 이용하지 않음.
    # 가장 작은 인덱스만 뽑아와서 비교함.

    # XXX: INF 값으로 채워진 0번을 최소 인덱스로 이용하면 편함.
    min_index = 0
    for i in range(1, len(table)):
        if not visited[i] and table[min_index] > table[i]:
            min_index = i
    return min_index


def dijkstra_simple(graph: list[list[int]], start: int) -> list[int]:
    N = len(graph)
    table = [INF] * N
    table[start] = 0
    # XXX: 큐처럼 이전에 체크한 요소를 빼지 않기 때문에,
    # 이전에 체크한 걸 따로 기록하는 리스트가 필요함.
    # XXX: 초기값 방문은 검색 후에 이뤄져야 함.
    visited = [False] * N

    for _ in range(N - 1):
        start = find_shortest_node(table, visited)
        visited[start] = True

        for v, e in graph[start]:
            table[v] = min(table[v], table[start] + e)

    return table


graph = [
    [],
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    [],
]

result = dijkstra_simple(graph, 1)
print(result[1:])

# 0, 2, 3, 1, 2, 4
