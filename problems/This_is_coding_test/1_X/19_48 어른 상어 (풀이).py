"""
1. 웬만하면 전역변수 이용하는 게 편함. (main 쓰면 인자 넘겨야 해서 복잡해짐)
2. 이에 따라 함수는 작은 것부터 먼저 만들게 됨.
3. N 크기가 작으면, 일일이 순회하면서 확인하는 게 쉬움. (냄새나, 현재 남은 상어 번호 등)
4. 겹치는 경우, 임시 배열을 만들어서 확인하기
"""

n, m, k = map(int, input().split())

# 모든 상어의 위치 리스트
arr = [list(map(int, input().split())) for _ in range(n)]

# 모든 상어의 현재 방향 정보
directions = list(map(int, input().split()))

# 각 상어마다 회전 우선순위 정보
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

# XXX: 각 위치마다 [상어 번호, 남은 시간] 저장
smells = [[[0, 0]] * n for _ in range(n)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


# XXX: 모든 냄새 정보 업데이트
def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하면, 시간 -1 감소
            if smells[i][j][1] > 0:
                smells[i][j][1] -= 1
            # 상어가 있으면 시간을 k로 재설정
            if arr[i][j] != 0:
                smells[i][j] = [arr[i][j], k]


# 모든 상어 이동
def move():
    # 이동 결과를 담기 위한 임시 결과 테이블
    n_arr = [[0] * n for _ in range(n)]

    # 각 위치를 하나씩 확인하며
    for row in range(n):
        for col in range(n):
            shark = arr[row][col]
            # 상어가 존재하는 경우
            if shark != 0:
                # 현재 상어의 방향
                direction = directions[shark - 1]
                priority_by_shark = priorities[shark - 1]
                # 현재 상어의 회전 우선순위
                priority_by_dir = priority_by_shark[direction - 1]

                is_smell_found = False
                # 일단 냄새가 존재하지 않는 곳 있는지 확인
                for d in priority_by_dir:
                    y = row + dy[d - 1]
                    x = col + dx[d - 1]
                    if not (0 <= y < n and 0 <= x < n):
                        continue

                    # 냄새가 없는 곳이면 (시간이 0)
                    if smells[y][x][1] == 0:
                        # 상어 방향 바꾸기
                        directions[shark - 1] = d
                        # 이동한 상어가 없는 경우, 상어 이동시키기
                        if n_arr[y][x] == 0:
                            n_arr[y][x] = shark
                        # 만약 다른 상어가 있다면, 더 낮은 번호 상어 넣기
                        else:
                            n_arr[y][x] = min(n_arr[y][x], shark)
                        is_smell_found = True
                        break

                if is_smell_found:
                    continue

                # 주변에 모두 냄새가 있던 경우, 자신의 냄새가 있던 곳으로 이동
                for d in priority_by_dir:
                    y = row + dy[d - 1]
                    x = col + dx[d - 1]

                    if not (0 <= y < n and 0 <= x < n):
                        continue

                    # XXX: 앞 단계에서 냄새가 전부 있단 걸 확인했으므로, 여기서는 번호만 확인.
                    # 자신의 냄새가 있던 곳이면
                    if smells[y][x][0] == shark:
                        # 방향 바꾸기
                        directions[shark - 1] = d
                        # 상어 이동하고 종료
                        n_arr[y][x] = shark
                        break

    return n_arr


time = 0
while time < 1000:
    update_smell()  # 모든 위치의 냄새 업데이트
    n_arr = move()  # 모든 상어 이동
    arr = n_arr  # 맵 업데이트
    time += 1

    # 1번 상어만 남았는지 체크
    check = True
    for row in range(n):
        for col in range(n):
            if arr[row][col] > 1:
                check = False

    if check:
        break

if time < 1000:
    print(time)
else:
    print(-1)
