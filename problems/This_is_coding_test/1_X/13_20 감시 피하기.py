from itertools import combinations


N = int(input())
arr = [input().split() for _ in range(N)]

# 빈 좌표와 선생님들 좌표를 미리 파악해놓기
blanks = []
teachers = []
for row in range(N):
    for col in range(N):
        value = arr[row][col]
        if value == 'X':
            blanks.append((row, col))
        elif value == 'T':
            teachers.append((row, col))

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def check_is_evadable_from_teacher(teacher: tuple[int, int]) -> bool:
    row = teacher[0]
    col = teacher[1]

    # 4방향 각각에 대해 조사
    for i in range(4):
        y = row
        x = col
        while True:
            # 각 방향 쪽으로 한 칸 나아감
            y += dy[i]
            x += dx[i]
            # 범위 벗어나면 스킵
            if not (0 <= y < N and 0 <= x < N):
                break
            # 장애물 만나도 스킵
            if arr[y][x] == 'O':
                break
            # 학생을 만나면, 선생으로부터 감시 피할 수 없음
            if arr[y][x] == 'S':
                return False

    # 모든 방향에 대해 조사했으므로, 해당 선생으로부터 감시 피할 수 있음
    return True


def check_evadable() -> bool:
    # 빈 좌표에서 3개를 뽑는 조합
    for obstacles in combinations(blanks, 3):
        # 각 좌표마다 장애물 설치
        for row, col in obstacles:
            arr[row][col] = 'O'

        is_evadable = False
        # 각 선생마다 감시 피할 수 있는지 확인
        for teacher in teachers:
            is_evadable = check_is_evadable_from_teacher(teacher)
            if not is_evadable:
                break
        # 모든 선생에게서 감시 피할 수 있으므로, 해당하는 조합이 있음.
        if is_evadable:
            return True

        # 다시 장애물 원래대로 복구
        for row, col in obstacles:
            arr[row][col] = 'X'

    # 모든 조합을 조사했으나, 감시 피할 수 없음
    return False


# 감시 피할 수 있는지 조사
is_evadable = check_evadable()
if is_evadable:
    print('YES')
else:
    print('NO')


"""
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
"""  # YES
"""
4
S S S T
X X X X
X X X X 
T T T X
"""  # NO
