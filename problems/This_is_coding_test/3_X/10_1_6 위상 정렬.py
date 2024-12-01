"""
## 방법
큐에 0인 것 넣기

## 예외
1. 여러 개 가능 -> 큐 길이가 2 이상
2. 사이클 -> 진입 차수 1 이상들만 남음.
-> 모든 원소 방문 전에 큐가 비어서 종료
-> 반환 수 부족

## 기타
무방향도 위상 정렬이 되나?
=> 안 됨. 어떤 정점이 다른 정점보다 먼저 와야 한다는
관계를 정의할 수가 없기 때문.
(= 순서를 정할 수 없기 때문에, "정렬" 불가)
"""
from collections import deque


def topology_sort(graph: list[list[int]]) -> list[int]:
    start = 1
    n = len(graph)

    ins = [0] * n
    # 인접 리스트 형식 그래프 가정
    for v in range(start, n):
        for w in graph[v]:
            ins[w] += 1

    queue = deque([])
    # X: visited 대신에 ins로 판별
    for v in range(start, n):
        if ins[v] == 0:
            queue.append(v)

    result = []
    while queue:
        # if len(queue) > 1:
        #     print("여러 개 가능")
        #     return []

        v = queue.popleft()
        result.append(v)

        for w in graph[v]:
            # XXX: 이론적으로 음수가 될 일이 없음.
            # 들어오는 간선이 음수 개가 된다는 건데, 말이 안 됨.
            # if ins[w] <= 0:
            #     continue

            ins[w] -= 1
            if ins[w] == 0:
                queue.append(w)

    if len(result) < n - start:
        print("사이클")
        return []
    else:
        return result


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)

result = topology_sort(graph)
print(result)

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
"""  # 1 2 5 3 6 4 7
