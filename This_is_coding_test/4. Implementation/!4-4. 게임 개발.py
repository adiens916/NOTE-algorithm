import sys
sys.stdin = open(f'3. 게임 개발.txt')


# 북, 동, 남, 서
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

def dfs(row, col, direct):
    global count

    used[row][col] = True
    count += 1

    for i in range(4):
        offset = (direct - 1 - i) % 4
        y = row + dy[offset]
        x = col + dx[offset]

        if not (0 <= x < N and 0 <= y < M):
            continue
        if arr[y][x] or used[y][x]:
            continue
        dfs(y, x, offset)

    
N, M = map(int, input().split())
row, col, direct = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

used = [[False] * M for _ in range(N)]
count = 0

dfs(row, col, direct)
print(count)
