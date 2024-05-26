# 반례 및 아이디어 참고: https://velog.io/@fill0006/백준-16236파이썬-아기상어
# 코드 구성 참고: https://aia1235.tistory.com/35

from collections import deque

SHARK = 9
# 방향은 상좌우하...가 아녀도 상관 없음.
# XXX: 우선순위라서 정렬로 해결할 거임.
dy = (-1, 0, 0, 1)
dx = (0, -1, 1, 0)


def main():
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    # 상어 정보
    total_time = 0
    size = 2
    eat = 0
    row, col = get_start(area, N)
    area[row][col] = 0

    # 가장 가까운 물고기 = BFS
    while True:
        targets = find_targets(area, N, row, col, size)
        # 더 이상 먹을 수 없으면 종료
        if not any(targets):
            print(total_time)
            break

        # XXX: 대상을 걸린 시간 - Y축 - X축 순으로 정렬
        targets.sort()
        # 가장 가까이 있는 물고기 구하기
        time, y, x = targets[0]
        # 잡아 먹기
        total_time += time
        area[y][x] = 0
        eat += 1
        # 자기 크기만큼 먹으면 크기 += 1
        if eat == size:
            size += 1
            eat = 0

        # 먹고 나면 다시 해당 지점을 시작점으로 BFS
        row, col = y, x


def get_start(area: list[list[int]], n: int) -> tuple[int, int]:
    for row in range(n):
        for col in range(n):
            if area[row][col] == SHARK:
                return row, col


def find_targets(area, n, row, col, size) -> list[tuple[int, int, int]]:
    # 잡아 먹을 수 있는 물고기 담아 놓을 배열
    eatables = []

    visited = [[False] * n for _ in range(n)]
    visited[row][col] = True
    time = 0

    queue = deque([(row, col, time)])
    while queue:
        row, col, time = queue.popleft()

        for i in range(4):
            y = row + dy[i]
            x = col + dx[i]

            if not (0 <= y < n and 0 <= x < n):
                continue
            if visited[y][x]:
                continue
            visited[y][x] = True

            target = area[y][x]
            # 크면 못 지나감
            if target > size:
                continue
            # 같으면 지나감
            elif target == 0 or target == size:
                queue.append((y, x, time + 1))
            # 작으면 먹을 수 있음
            else:
                eatables.append((time + 1, y, x))

    # (걸린 시간, Y축, X축) 리스트 반환
    return eatables


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
