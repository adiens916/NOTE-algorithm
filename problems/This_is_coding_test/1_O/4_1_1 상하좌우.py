N = int(input())
plan_list = input().split()

X, Y = 1, 1
move_types = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

for plan in plan_list:
    move = move_types.get(plan)
    if 1 <= X + move[0] <= N and 1 <= Y + move[1] <= N:
        X += move[0]
        Y += move[1]

print(X, Y)
