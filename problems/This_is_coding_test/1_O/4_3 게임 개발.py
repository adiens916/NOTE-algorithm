N, M = map(int, input().split())
A, B, d = map(int, input().split())

game_map = []
for i in range(N):
    map_line = list(map(int, input().split()))
    game_map.append(map_line)

move_types: dict[int, tuple[int, int]] = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}


def turn_left(d: int) -> int:
    return ((d - 1) + 4) % 4


def is_able_to_go_forward(y: int, x: int) -> bool:
    return game_map[y][x] != 1 and game_map[y][x] != -1


def is_visited_all_around(a: int, b: int) -> bool:
    for move in move_types.values():
        y = a + move[0]
        x = b + move[1]
        if is_able_to_go_forward(y, x):
            return False
    return True


count = 0
while True:
    if not is_visited_all_around(A, B):
        d = turn_left(d)

        move = move_types.get(d)
        y = A + move[0]
        x = B + move[1]
        if is_able_to_go_forward(y, x):
            A = y
            B = x
            game_map[A][B] = -1
            count += 1
    else:
        move = move_types.get(d)
        y = A - move[0]
        x = B - move[1]
        if game_map[y][x] == 1:
            break
        else:
            A, B = y, x

print(count)


"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
