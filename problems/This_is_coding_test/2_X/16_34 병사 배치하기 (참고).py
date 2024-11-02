from bisect import bisect_left


N = int(input())
powers = list(map(int, input().split()))

# 뒤집어주는 이유는 bisect_left 때문.
powers.reverse()
max_lens = [powers[0]]

for i in range(1, N):
    if max_lens[-1] < powers[i]:
        max_lens.append(powers[i])

    else:
        # XXX: bisect_left는 오름차순으로 정렬된 때를 기준으로 함.
        # 그래서 문제에서처럼 내림차순이면 인덱스를 아예 벗어남.
        # ⇒ 전부 반대로 해야 함 (reverse를 하고, 클 때만 추가하는 등)
        idx = bisect_left(max_lens, powers[i])

        # 인덱스 교체. 실제 수열과는 다를 수 있음. 그러나 상관없다.
        # 1. 일단 길이만 보는 것이고
        # 2. 맨 마지막 원소만 기준으로 비교하는 것이기 때문.
        max_lens[idx] = powers[i]

print(N - len(max_lens))
