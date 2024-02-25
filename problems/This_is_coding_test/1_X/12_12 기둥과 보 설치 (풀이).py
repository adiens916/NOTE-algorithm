COL = 0
ROW = 1

DEL = 0
CON = 1


def can_build_column(answer, x, y) -> bool:
    # 바닥 위
    if y == 0:
        return True
    # 좌측에 보가 있는 경우
    # XXX: 해당 기둥/보가 현재 구조물에 있는지 확인만 하면 되기에, 범위 체크가 필요없음.
    if [x - 1, y, ROW] in answer:
        return True
    # 우측에 보가 있는 경우
    if [x, y, ROW] in answer:
        return True
    # 다른 기둥 위
    if [x, y - 1, COL] in answer:
        return True
    return False


def can_build_row(answer, x, y) -> bool:
    # 좌측 끝이 기둥 위
    if [x, y - 1, COL] in answer:
        return True
    # 우측 끝이 기둥 위
    if [x + 1, y - 1, COL] in answer:
        return True
    # 양쪽 끝부분이 다른 보와 동시에 연결
    if [x - 1, y, ROW] in answer and [x + 1, y, ROW] in answer:
        return True
    return False


def possible(answer: list) -> bool:
    for x, y, stuff in answer:
        if stuff == COL:
            # 어느 한 기둥/보가 성립하지 않으면 False
            if not can_build_column(answer, x, y):
                return False

        if stuff == ROW:
            if not can_build_row(answer, x, y):
                return False

    return True


def solution(n, build_frame) -> list:
    answer = []

    for x, y, stuff, work in build_frame:
        if work == CON:
            answer.append([x, y, stuff])
            # XXX: 현재 구조물 '전체'가 성립하는지 확인
            if not possible(answer):
                answer.remove([x, y, stuff])

        if work == DEL:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])

    # XXX: x, y, 기둥-보 순으로 오름차순 정렬이므로 정렬 함수 그대로 적용 가능
    return sorted(answer)


def case_1():
    n = 5
    build_frame = [
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [2, 1, 0, 1],
        [2, 2, 1, 1],
        [5, 0, 0, 1],
        [5, 1, 0, 1],
        [4, 2, 1, 1],
        [3, 2, 1, 1],
    ]
    result = solution(n, build_frame)

    expected = [
        [1, 0, 0],
        [1, 1, 1],
        [2, 1, 0],
        [2, 2, 1],
        [3, 2, 1],
        [4, 2, 1],
        [5, 0, 0],
        [5, 1, 0],
    ]

    print(result)


case_1()


def case_2():
    n = 5
    build_frame = [
        [0, 0, 0, 1],
        [2, 0, 0, 1],
        [4, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [2, 1, 1, 1],
        [3, 1, 1, 1],
        [2, 0, 0, 0],
        [1, 1, 1, 0],
        [2, 2, 0, 1],
    ]
    result = solution(n, build_frame)

    expected = [
        [0, 0, 0],
        [0, 1, 1],
        [1, 1, 1],
        [2, 1, 1],
        [3, 1, 1],
        [4, 0, 0],
    ]

    print(result)


case_2()
