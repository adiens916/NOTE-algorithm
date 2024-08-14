from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1

    # 원형 -> 일렬로 펼치기
    W = len(weak)
    for i in range(W):
        weak.append(weak[i] + n)

    for start in range(W):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            end = weak[start] + friends[count - 1]

            for point in range(start, start + W):
                if end < weak[point]:
                    count += 1
                    if count > len(friends):
                        break
                    end = weak[point] + friends[count - 1]

            answer = min(answer, count)

    if answer == len(dist) + 1:
        answer = -1
    return answer
