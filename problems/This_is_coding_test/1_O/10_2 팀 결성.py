def find_parent(x: int, parents: list[int]) -> int:
    if parents[x] != x:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


def union_parent(a: int, b: int, parents: list[int]) -> None:
    a = find_parent(a, parents)
    b = find_parent(b, parents)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N, M = map(int, input().split())
team_nums = [i for i in range(N + 1)]

commands = [list(map(int, input().split())) for _ in range(M)]

for command, a, b in commands:
    if command == 0:  # union
        union_parent(a, b, team_nums)

    elif command == 1:  # check
        a_team = find_parent(a, team_nums)
        b_team = find_parent(b, team_nums)
        if a_team == b_team:
            print("YES")
        else:
            print("NO")


"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""
