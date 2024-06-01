def solution(food_times: list[int], K: int):
    MAX = 100000000
    while True:
        min_time = MAX
        for time in food_times:
            if time > 0:
                min_time = min(min_time, time)

        expected_time = 0
        remaining_foods = []
        for i in range(len(food_times)):
            if food_times[i] > 0:
                food_times[i] -= min_time
                expected_time += min_time
                remaining_foods.append(i)

        if expected_time < K:
            K -= expected_time
        else:
            break

    is_found = False
    while not is_found:
        for food_num in remaining_foods:
            food_times[food_num] -= 1
            K -= 1

            if K == 0:
                is_found = True
                break

            if food_times[food_num] == 0:
                remaining_foods.remove(food_num)

        if is_found:
            answer = food_num + 1
            break

    return answer


print(solution([3, 1, 2], 5))
