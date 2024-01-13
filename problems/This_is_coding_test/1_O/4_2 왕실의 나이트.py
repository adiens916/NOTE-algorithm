def chr_to_int(chr: str) -> int:
    return ord(chr) - ord("a") + 1


move_types = [
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
    (2, -1),
    (2, 1),
    (-2, -1),
    (-2, 1),
]

start = input().strip()
x, y = chr_to_int(start[0]), int(start[1])

count = 0
for move in move_types:
    if 1 <= x + move[0] <= 8 and 1 <= y + move[1] <= 8:
        count += 1

print(count)
