from collections import deque


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def bfs(arr: list[list[int]], visited: list[list[bool]], row: int, col: int):
    q = deque([(row, col)])
    visited[row][col] = True
    allies_loc = [(row, col)]
    allies_people = arr[row][col]
    allies_num = 1

    while q:
        row, col = q.popleft()

        for i in range(4):
            y = row + dirs[i][1]
            x = col + dirs[i][0]

            if not (0 <= y < N and 0 <= x < N):
                continue
            if visited[y][x]:
                continue

            diff = abs(arr[y][x] - arr[row][col])
            if not (L <= diff <= R):
                continue

            visited[y][x] = True
            q.append((y, x))

            allies_num += 1
            allies_people += arr[y][x]
            allies_loc.append((y, x))

    if allies_num == 1:
        return False

    else:
        allies_people_avg = allies_people // allies_num
        for row, col in allies_loc:
            arr[row][col] = allies_people_avg
        return True


move_count = 0
is_moved = False

while True:
    visited = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if not visited[row][col]:
                result = bfs(arr, visited, row, col)

                if result:
                    is_moved = True

    if is_moved:
        move_count += 1
        is_moved = False
    else:
        print(move_count)
        break


"""
2 20 50
50 30
20 40
"""  # 1
"""
2 40 50
50 30
20 40
"""  # 0
"""
3 5 10
10 15 20
20 30 25
40 22 10
"""  # 2
"""
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
"""  # 3
