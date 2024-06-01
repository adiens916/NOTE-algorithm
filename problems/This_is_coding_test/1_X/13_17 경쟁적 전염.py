N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())


def pick_viruses(arr) -> list[tuple[int, int, int, int]]:
    queue = []
    cur_time = 0

    for row in range(N):
        for col in range(N):
            virus_num = arr[row][col]
            if virus_num > 0:
                queue.append((virus_num, cur_time, row, col))

    queue.sort()
    return queue


def bfs(arr: list[list[int]], max_t: int) -> None:
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    queue = pick_viruses(arr)

    while any(queue):
        virus, cur_time, row, col = queue.pop(0)

        if cur_time == max_t:
            break

        for i in range(4):
            y = row + dy[i]
            x = col + dx[i]
            if not (0 <= y < N and 0 <= x < N):
                continue
            if arr[y][x] > 0:
                continue
            arr[y][x] = virus
            queue.append((virus, cur_time + 1, y, x))


bfs(arr, S)
print(arr[X - 1][Y - 1])


"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2
"""  # 3
"""
3 3
1 0 2
0 0 0
3 0 0
1 2 2
"""  # 0
