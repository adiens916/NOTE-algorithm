"""
인구 이동 없을 때까지 지속
인구 차이가 L명 이상, R명 이하
연합 인구 수 / 연합 칸의 개수 (소수점은 버림)
인구 이동 몇 번 일어나는지

연합 찾기 = BFS
같은 날 중엔 이미 체크한 곳은 지나가야 함
"""

from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def bfs(r, c, visited):
    union = [(r, c)]
    union_sum = arr[r][c]

    visited[r][c] = True
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            y = r + dy[i]
            x = c + dx[i]

            if not (0 <= y < N and 0 <= x < N):
                continue

            # XXX: 방문 여부보다 연결이 가능한지부터 체크해야 함.
            # 왜냐하면 같은 지점이어도 어느 곳에서부터 접근했는지에 따라
            # 연결이 될 수도 안 될 수도 있기 때문.
            diff = abs(arr[y][x] - arr[r][c])
            if not L <= diff <= R:
                continue

            if visited[y][x]:
                continue
            visited[y][x] = True
            queue.append((y, x))
            union.append((y, x))
            union_sum += arr[y][x]

    if len(union) == 1:
        return False

    new_pop = union_sum // len(union)
    for r, c in union:
        arr[r][c] = new_pop
    return True


for day in range(0, 2001):
    visited = [[False] * N for _ in range(N)]
    is_moved = False

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                result = bfs(r, c, visited)
                if result:
                    is_moved = True

    if not is_moved:
        print(day)
        break
