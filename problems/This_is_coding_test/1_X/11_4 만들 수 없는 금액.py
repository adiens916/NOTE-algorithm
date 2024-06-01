# XXX: 답은 맞는 거 같은데, 시간 복잡도가 대략 1,000 * 1,000,000으로 큼.
# 그래서 풀이를 봤는데 이해가 안 됨...
# => 나중에 다시 보기

N = int(input())
coin_list = list(map(int, input().split()))

coin_list.sort(reverse=True)

for target in range(1, 1000001):
    cur_sum = 0

    # 가장 큰 단위부터 체크
    for coin in coin_list:
        # 목표 금액보다 큰 경우, 해당 단위는 넘기고, 더 작은 단위 체크
        if cur_sum + coin > target:
            continue

        # 작은 단위면 더하기
        cur_sum += coin
        # 만약 목표 금액과 같으면 나오기
        if cur_sum == target:
            break

    # 목표 금액 만들 수 없으면, 바로 그 값이 최솟값임.
    if cur_sum != target:
        print(target)
        break


"""
5
3 2 1 1 9
"""  # 8
"""
3
3 5 7
"""  # 1
