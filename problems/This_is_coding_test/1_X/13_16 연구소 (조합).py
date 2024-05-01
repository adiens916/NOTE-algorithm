MAX = 6
N = 3


def combination(depth: int, count: int, result: list[int]) -> None:
    if count == N:
        print(result)
        return

    for i in range(depth, MAX):
        result.append(i)
        combination(i + 1, count + 1, result)
        result.pop()


# combination(0, 0, [])


arr = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
]
row = 3
col = 4


def combination_2d(depth: int, count: int, result: list[tuple[int, int]]) -> None:
    if count == N:
        # print(result)
        print([arr[y][x] for y, x in result])
        return

    for i in range(depth, row * col):
        y = i // col
        x = i % col

        result.append((y, x))
        combination_2d(i + 1, count + 1, result)
        result.pop()


combination_2d(0, 0, [])
