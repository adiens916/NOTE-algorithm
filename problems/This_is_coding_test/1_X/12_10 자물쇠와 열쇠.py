def rotate_clockwise(arr) -> list:
    L = len(arr)
    new_arr = [[0] * L for _ in range(L)]

    for col in range(L):
        for row in range(L - 1, -1, -1):
            new_arr[col][L - 1 - row] = arr[row][col]

    return new_arr


def get_value_in_proper_range(arr, y, x, L):
    if 0 <= y < L and 0 <= x < L:
        return arr[y][x]
    else:
        return 0


def match_key_with_lock(key, lock):
    K = len(key)
    L = len(lock)

    for dy in range(K - 1, -L, -1):
        for dx in range(K - 1, -L, -1):
            is_all_matched = True

            for y in range(L):
                for x in range(L):
                    lock_val = lock[y][x]
                    key_val = get_value_in_proper_range(key, y + dy, x + dx, K)
                    if lock_val + key_val != 1:
                        is_all_matched = False
                        break

                # 한 번이라도 어긋났으면 빠져 나오기
                if not is_all_matched:
                    break

            # 자물쇠 다 살펴봤는데 어긋난 게 없으면 True 반환
            if is_all_matched:
                return True

    # 키를 전부 옮겼는데도 맞는 게 없으면 False
    return False


def solution(key, lock):
    key_90 = rotate_clockwise(key)
    key_180 = rotate_clockwise(key_90)
    key_270 = rotate_clockwise(key_180)

    for key_ in (key, key_90, key_180, key_270):
        matched = match_key_with_lock(key_, lock)
        if matched:
            return True

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
