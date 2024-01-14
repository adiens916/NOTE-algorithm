def dfs(start: int, graph: list[list[int]], visited: list[int]) -> None:
    # XXX: 방문 체크를 미리 안 하고, for 반복문 안에서 할 수도 있음.
    # 그러면 쓸데없는 함수 호출을 줄여서 더 빠름.
    # 그래도 이렇게 먼저 체크하는 편이 훨씬 직관적이고 깔끔해서 맘에 듦.
    if visited[start]:
        return

    visited[start] = True
    print(start, end=" ")

    for v in graph[start]:
        dfs(v, graph, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * (len(graph) + 1)

dfs(1, graph, visited)
print()


def dfs_without_recursive(start, graph, visited):
    # XXX: 재귀 함수를 이용하지 않고도 가능
    # 다만, 함수는 하나씩 처리하는 반면, 반복문은 일단 다 넣고 처리하는 게 차이.
    # 이로 인해 처리 순서가 달라지게 됨. (큰 게 나중에 들어오니, 큰 것부터 처리하게 됨)
    stack = [start]

    while any(stack):
        start = stack.pop()

        if visited[start]:
            continue
        visited[start] = True
        print(start, end=" ")

        for v in graph[start]:
            stack.append(v)


# XXX: 재귀 함수로 넘길 필요도 없으므로, 함수 안에 선언해도 됨.
visited = [False] * (len(graph) + 1)

dfs_without_recursive(1, graph, visited)
