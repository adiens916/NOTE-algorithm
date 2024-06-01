# N * N 크기
# M개의 서로 다른 번호들
# 처음 위치에 자기 냄새
# 이동 후 바로 자기 냄새 남김
# 상어랑 냄새 따로 => 상어 배열 따로

# 냄새 없는 칸 - 자신의 냄새 있는 칸 - 특정 우선순위 (상어, 방향)
# 이동한 '방향' => 보고 있는 방향

# 한 칸에 여러 마리 있을 시, 가장 작은 번호의 상어만 남음
# => 겹치는 거 파악하고, 겹칠 시 작은 상어만 남김

# 냄새는 k번 이동하고 나면 사라짐
# => 일단 이동 후 k+1만큼 남기고, 맵 전체 냄새 줄이기

# 1번 상어만 격자에 남을 때까지 걸리는 시간
# 1000초 넘어도 다른 상어 있으면 -1
# => 상어 개수 따로 카운트?

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def main():
    n, m, k = map(int, input().split())

    arr = [(0, 0) for x in range(n) for y in range(n)]
    sharks = [(-1, -1) for _ in range(m + 1)]
    for row in range(n):
        line = list(map(int, input().split()))
        for col in range(n):
            shark_num = line[col]
            if shark_num > 0:
                arr[row][col] = (shark_num, k)
                sharks[shark_num] = (row, col)

    ways = list(map(int, input().split()))
    ways.insert(0, 0)

    next_ways = [[(), (), (), ()] for _ in range(m + 1)]
    for i in range(1, m + 1):
        p = [tuple(map(int, input().split())) for _ in range(4)]
        next_ways[i] = p

    t = 0
    while t < 1000:
        remains = move_all_sharks(arr, sharks, ways, next_ways, n, k)
        if remains == 1:
            break
    if t < 1000:
        print(t)
    else:
        print(-1)


def move_all_sharks(arr, sharks, ways, next_ways, n, k) -> int:
    for row, col in sharks:
        if row == -1:
            continue
        pass
        # move_shark()


def move_shark(shark, arr, sharks, ways, next_ways, n, k):
    row, col = sharks[shark]
    way = ways[shark]

    for w in next_ways[shark][way - 1]:
        y = row + dy[w - 1]
        x = col + dx[w - 1]

        if not (0 <= y < n and 0 <= x < n):
            continue
        num = arr[y][x][0]
        odor = arr[y][x][1]
        if num == 0:
            occupy(shark, y, x, w, arr, sharks, ways, k)
            return 0
        if num < shark and odor == k + 1:
            escape(shark, sharks)
            return -1

    for w in next_ways[shark][way - 1]:
        y = row + dy[w - 1]
        x = col + dx[w - 1]

        if not (0 <= y < n and 0 <= x < n):
            continue
        if arr[y][x][0] == shark:
            occupy(shark, y, x, w, arr, sharks, ways, k)
            return 0


def occupy(shark, row, col, way, arr, sharks, ways, k):
    arr[row][col][0] = shark
    arr[row][col][1] = k
    sharks[shark] = (row, col)
    ways[shark] = way


def escape(shark, sharks):
    sharks[shark] = (-1, -1)


main()

"""
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
"""