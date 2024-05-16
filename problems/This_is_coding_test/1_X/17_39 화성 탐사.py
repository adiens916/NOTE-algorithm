import heapq


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        area = [list(map(int, input().split())) for _ in range(N)]
        answer = shortest_path(N, area)
        print(answer)


def shortest_path(n: int, area: list[list[int]]) -> int:
    INF = int(1e9)
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    # Init shortest path list
    shortest_nodes = [[INF] * n for _ in range(n)]
    # Set cost of start
    shortest_nodes[0][0] = area[0][0]

    # Init priority queue
    queue = [(area[0][0], 0, 0)]
    while queue:
        cur_cost, row, col = heapq.heappop(queue)

        # Check visit
        # Because a shorter one might have been found in early steps
        prev_cost = shortest_nodes[row][col]
        if prev_cost < cur_cost:
            continue

        for i in range(4):
            y = row + dy[i]
            x = col + dx[i]

            # Check range
            if not (0 <= y < n and 0 <= x < n):
                continue

            # Compare distance
            new_cost = shortest_nodes[row][col] + area[y][x]
            if new_cost < shortest_nodes[y][x]:
                shortest_nodes[y][x] = new_cost
                heapq.heappush(queue, (new_cost, y, x))

    return shortest_nodes[n - 1][n - 1]


main()

"""
1
3
0 0 0
0 0 0
0 0 1
"""  # 1
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
"""  # 20 / 19 / 36
