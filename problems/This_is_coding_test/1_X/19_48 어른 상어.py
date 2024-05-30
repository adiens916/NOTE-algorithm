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

    arr = [list(map(int, input().split())) for _ in range(n)]
    sharks = [(-1, -1) for _ in range(m + 1)]
    for row in range(n):
        for col in range(n):
            if arr[row][col] > 0:
                shark = arr[row][col]
                sharks[shark] = (row, col)

    shark_ways = list(map(int, input().split()))
    shark_ways.insert(0, 0)

    shark_ps = [[(), (), (), ()] for _ in range(m + 1)]
    for i in range(1, m + 1):
        p = [tuple(map(int, input().split())) for _ in range(4)]
        shark_ps[i] = p


    move_shark()


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