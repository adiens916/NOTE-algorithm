def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    foods = [(food_times[i], i) for i in range(len(food_times))]

    foods.sort()
    prev_t = 0
    for i in range(len(foods)):
        cur_t = foods[i][0] - prev_t
        remain_num = len(foods) - i
        total_t = cur_t * remain_num

        if total_t <= k:
            k -= total_t
            prev_t = cur_t
        else:
            foods = foods[i:]
            break

    foods.sort(key=lambda x: x[1])
    # XXX: 나머지 연산 필요했음.
    # 총합으로만 비교했는데, 개수는 적고 음식량이 많을 수 있기 때문.
    target = k % len(foods)
    answer = foods[target][1]
    return answer + 1


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
