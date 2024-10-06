def solution(key, lock):
    K = len(key)
    L = len(lock)

    # 1. 자물쇠 늘리기
    new_lock = [[0] * (3 * L) for _ in range(3 * L)]
    for r in range(L):
        for c in range(L):
            new_lock[L + r][L + c] = lock[r][c]

    # 2. 회전 4번
    for rotation in range(4):
        key = rotate(key)

        # 3. 열쇠 시작 위치 고정
        # 맨 좌측 위 ~ 자물쇠 마지막 걸칠 때까지
        for r in range(2 * L):
            for c in range(2 * L):

                for y in range(K):
                    for x in range(K):
                        new_lock[r+y][c+x] += key[y][x]

                # 4. 체크
                if is_matched(new_lock):
                    return True

                for y in range(K):
                    for x in range(K):
                        new_lock[r + y][c + x] -= key[y][x]

    return False


def rotate(key):
    K = len(key)
    new_key = [[0] * K for _ in range(K)]

    for y in range(K):
        for x in range(K):
            # [x][K - 1 - y]
            new_key[x][K - 1 - y] = key[y][x]

    return new_key


def is_matched(lock):
    # 범위 정하기
    L = len(lock)
    start = L // 3
    end = L // 3 * 2

    for y in range(start, end):
        for x in range(start, end):
            if lock[y][x] != 1:
                return False

    return True


