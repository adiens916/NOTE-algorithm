"""
1, 1 부터 시작
빈 칸에 장애물 3개 설치
모든 학생들이 감시 피할 수 있는지
"""

N = int(input())
arr = [list(input().split()) for _ in range(N)]

blanks = []
teachers = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == "X":
            blanks.append((r, c))
        elif arr[r][c] == "T":
            teachers.append((r, c))


def watch():
    dy = (-1, 0, 1, 0)
    dx = (0, -1, 0, 1)

    for (r, c) in teachers:
        for i in range(4):
            while True:
                y = r + dy[i]
                x = c + dx[i]

                if not (0 <= y < N and 0 <= x < N):
                    break
                if arr[y][x] == "O":
                    break
                if arr[y][x] == "S":
                    return False

                r = y
                c = x

    return True


checked = [False] * len(blanks)
is_available = False


def combination(built):
    global is_available

    if built == 3:
        result = watch()
        if result is True:
            is_available = True
        return

    for i in range(len(checked)):
        if not checked[i]:
            checked[i] = True
            r, c = blanks[i]
            arr[r][c] = "O"
            combination(built + 1)
            arr[r][c] = "X"
            checked[i] = False


if is_available:
    print("YES")
else:
    print("NO")
