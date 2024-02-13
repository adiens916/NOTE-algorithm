import heapq


def solution(food_times: list[int], k: int) -> int:
    # XXX: 전체 먹는 시간보다 k가 크거나 같으면 답 없음
    if sum(food_times) <= k:
        return -1

    # XXX: 작은 걸 빠르게 찾기 위해 우선순위 큐 이용
    queue = [(food_times[i], i + 1) for i in range(len(food_times))]
    heapq.heapify(queue)

    prev_time = 0
    while any(queue):
        time, pos = queue[0]
        # 작은 것 기준으로 전체 시간을 계산
        expected_time = (time - prev_time) * len(queue)

        if expected_time <= k:
            k -= expected_time
            prev_time = time
            # XXX: k가 감소할 때만 큐에서 빼야 함 (먼저 빼면 안 됨)
            heapq.heappop(queue)
        else:
            break

    # XXX: 남은 음식 중에서 정렬
    queue.sort(key=lambda x: x[1])
    # XXX: 위치는 차분히 경우의 수를 써내려가면서 패턴 파악하기...
    pos = k % len(queue)
    answer = queue[pos][1]

    return answer


print(solution([3, 1, 2], 5))
