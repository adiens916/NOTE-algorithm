"""
다익스트라 최단 경로
cost(b) = min(cost(b), cost(a) + x)

상하좌우 1칸씩 이동
"""
import heapq

INF = int(1e9)
dy = (0, -1, 0, 1)
dx = (-1, 0, 1, 0)


def dijkstra_shortest_for_2d(graph: list[list[int]]) -> int:
    N = len(graph)

    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = graph[0][0]

    queue = [(dist[0][0], 0, 0)]

    while queue:
        cost, row, col = heapq.heappop(queue)
        if dist[row][col] < cost:
            continue

        for i in range(4):
            y = row + dy[i]
            x = col + dx[i]

            if not (0 <= y < N and 0 <= x < N):
                continue

            new_cost = dist[row][col] + graph[y][x]
            if dist[y][x] > new_cost:
                dist[y][x] = new_cost
                heapq.heappush(queue, (new_cost, y, x))

    return dist[N - 1][N - 1]


T = int(input())
for _ in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    result = dijkstra_shortest_for_2d(graph)
    print(result)


"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1 
1 2 1 8 1 
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3 
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""  # 20, 19, 36
