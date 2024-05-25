from collections import deque


SHARK = 9
# 방향은 상좌우하
dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)


def main():
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    # 상어 정보
    total_time = 0
    # 아기 상어 크기는 처음에 2
    size = 2
    eat = 0
    row, col = get_start(area, N)
    area[row][col] = 0

    # 가장 가까운 물고기 = BFS
    # 먹고 나면 다시 해당 지점을 시작점으로 BFS
    while True:
        visited = [[False] * N for _ in range(N)]
        visited[row][col] = True

        is_target_eaten = False
        queue = deque([(row, col, total_time)])
        while queue:
            row, col, time = queue.popleft()

            for i in range(4):
                y = row + dy[i]
                x = col + dx[i]

                if not (0 <= y < N and 0 <= x < N):
                    continue
                if visited[y][x]:
                    continue
                visited[y][x] = True

                target = area[y][x]
                # 크면 못 지나감, 같으면 지나감, 작으면 지나가면서 먹음
                if target > size:
                    continue
                elif target == 0 or target == size:
                    queue.append((y, x, time + 1))
                else:  # 0 < target < size
                    # 잡아먹기
                    area[y][x] = 0
                    eat += 1
                    # 자기 크기만큼 먹으면 크기 += 1
                    if eat == size:
                        size += 1
                        eat = 0

                    # 그 지점부터 다시 시작
                    row, col = y, x
                    total_time = time + 1
                    is_target_eaten = True
                    break

            # 잡아먹었으면 해당 지점부터 다시 BFS
            if is_target_eaten:
                break
        # 더 이상 먹을 수 없음
        if not is_target_eaten:
            break

    print(total_time)


def get_start(area: list[list[int]], n: int) -> tuple[int, int]:
    for row in range(n):
        for col in range(n):
            if area[row][col] == SHARK:
                return row, col


main()

"""
3
0 0 0
0 0 0
0 9 0
"""  # 0
"""
3
0 0 1
0 0 0
0 9 0
"""  # 3
"""
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
"""  # 14
"""
6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
"""  # 60
