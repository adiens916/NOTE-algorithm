from itertools import permutations


def partial_solution(start, n, weak, dist):
    # 방문 여부와 모두 돌았는지 카운트 체크
    visited = [False] * len(weak)
    v_count = 0

    # 친구 번호 & 카운트
    f_idx = 0
    f_count = len(dist)

    # 아직 다 안 돌았고 & 친구들도 남아있으면 계속 반복
    # XXX: 두 조건을 동시에 만족해야 함
    while v_count < len(weak) and f_count > 0:
        # 도착 지점
        dest = weak[start] + dist[f_idx]
        # 현재 지점이 도착 지점보다 앞에 있는 경우
        while weak[start] <= dest:
            # 방문한 경우 종료
            if visited[start]:
                break

            # 점검 완료
            visited[start] = True
            v_count += 1

            # 다음 지점으로 넘어가기
            start += 1
            if start == len(weak):
                start = 0
                dest -= n

        # 도착 지점을 넘어서는 경우, 친구 다 썼으므로 감소
        f_count -= 1
        f_idx += 1

    # 만약 남아있는 친구가 없는데 덜 돈 경우, 점검 불가
    if f_count == 0 and v_count < len(weak):
        return -1
    else:
        return len(dist) - f_count


def solution(n, weak, dist):
    min_count = len(dist)
    is_possible = False
    dist_list = list(permutations(dist, len(dist)))

    for start in range(len(weak)):
        # XXX: 무조건 거리가 긴 애부터 내림차순으로 배치하는 게 아님.
        # 중간에 짧은 곳이 나오면, 이동 거리가 짧은 애를 적재적소에 배치해야 더 효율적
        # 즉, 내림차순이 아닌 순열로 풀어야 함.
        # 출처: https://school.programmers.co.kr/questions/38554
        for cur_dist in dist_list:
            count = partial_solution(start, n, weak, cur_dist)

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
    result = 2
    print(solution(n, weak, dist))


case_1()


def case_2():
    n = 100
    weak = [1, 50, 99]
    dist = [1, 2]
    result = 2
    print(solution(n, weak, dist))


case_2()


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
