"""
스테이지: 1, 2 2 2, 3 3, 4, 6
실패율: 1/8, 3/(8-1), 2/(8-4), 1/(8-6), 0
"""


def solution(N: int, stages: list):
    people = len(stages)

    # 계수 정렬 이용
    counts = [0] * (N + 2)
    for stage in stages:
        counts[stage] += 1

    failures = []
    count_sum = 0
    # 1번부터 N번째 스테이지까지 순회
    for i in range(1, N + 1):
        # 해당 스테이지 도전자가 없으면 실패율 0
        if counts[i] == 0:
            failure_rate = 0
        else:
            # 실패율은 해당 스테이지 도전자 수 / (전체 - 이전까지 도전자 수)
            failure_rate = counts[i] / (people - count_sum)
            # 남은 도전자 수 줄이기
            count_sum += counts[i]

        # 실패율 배열에 넣기. 이때 내림차순이므로, 실패율에는 - 붙이기.
        failures.append((-failure_rate, i))

    # 정렬. 실패율은 - 가 붙으므로 큰 값이 먼저 옴.
    # 두 번째 인자는 스테이지 번호이므로, 스테이지 번호는 오름차순 정렬됨.
    failures.sort()
    answer = [failure[1] for failure in failures]

    return answer
