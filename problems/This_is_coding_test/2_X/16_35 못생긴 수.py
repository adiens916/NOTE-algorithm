import heapq


def ugly_num(n: int) -> int:
    result = []
    queue = [1]

    while len(result) <= n:
        min_ugly = heapq.heappop(queue)
        # XXX: 추가하는 과정에서 중복으로 추가됨 => 중복 제거 필요.
        # 어차피 항상 최솟값을 가져올 테고, 이는 최근에 추가한 것과 같을 거임.
        if len(result) > 0 and min_ugly == result[-1]:
            continue
        result.append(min_ugly)

        heapq.heappush(queue, min_ugly * 2)
        heapq.heappush(queue, min_ugly * 3)
        heapq.heappush(queue, min_ugly * 5)

    return result[n - 1]


N = int(input())
print(ugly_num(N))
