def partial_solution(start, n, weak, dist):
    visited = [False] * len(weak)
    v_count = 0

    f_idx = len(dist) - 1
    f_count = len(dist)

    # XXX: 두 조건을 동시에 만족해야 함
    while v_count < len(weak) and f_count > 0:
        dest = weak[start] + dist[f_idx]
        while weak[start] <= dest:
            if visited[start]:
                break

            visited[start] = True
            v_count += 1

            start += 1
            if start == len(weak):
                start = 0
                dest -= n

        f_count -= 1
        f_idx -= 1

    if f_count == 0 and v_count < len(weak):
        return -1
    else:
        return len(dist) - f_count


def solution(n, weak, dist):
    min_count = len(dist)
    is_possible = False

    for start in range(len(weak)):
        count = partial_solution(start, n, weak, dist)

        # XXX: 시작 지점에 따라서 될 수도 있고 안 될 수도 있음.
        # 되는 경우가 있는지 & 그 때의 값을 출력해야 함.
        if count != -1:
            is_possible = True
            min_count = min(min_count, count)

    if is_possible:
        return min_count
    else:
        return -1


def case_1():
    n = 12
    weak = [1, 5, 6, 10]
    dist = [1, 2, 3, 4]
    print(solution(n, weak, dist))


# case_1()


def case_2():
    n = 100
    weak = [1, 50, 99]
    dist = [1, 2]
    print(solution(n, weak, dist))


# case_2()


def case_3():
    # XXX: 1번부터 시작해서 시계방향으로 4, 1, 2, 1 순서로 사람을 보내야 함.
    # 즉, 내림차순으로 푸는 게 아니라, 적재적소에 맞게 배치해야 함 ⇒ 순열
    # 출처: https://school.programmers.co.kr/questions/38554
    n = 16
    weak = [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 14, 15]
    dist = [4, 2, 1, 1]
    result = 4
    print(solution(n, weak, dist))


case_3()
