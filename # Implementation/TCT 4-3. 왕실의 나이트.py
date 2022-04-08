row, col = list(input())
row = ord(row) - ord('a') + 1
col = int(col)

# 상 하 좌 우. 두 칸씩 간 후 두 갈래로 파생
dy = (-2, -2, 2, 2, -1, 1, -1, 1)
dx = (-1, 1, -1, 1, -2, -2, 2, 2)

count = 0
for i in range(len(dx)):
    y = row + dy[i]
    x = col + dx[i]
    if 1 <= x <= 8 and 1 <= y <= 8:
        count += 1

print(count)
