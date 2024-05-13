"""
Idea 1: https://velog.io/@dltmdrl1244/알고리즘-백준-15483파이썬-편집-거리Edit-Distance-알고리즘
Idea 2: https://joyjangs.tistory.com/38
"""

A = input()
B = input()

# 2d Array Declaration
edit_dist = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

# Initialization
for y in range(1, len(A) + 1):
    edit_dist[y][0] = y
for x in range(1, len(B) + 1):
    edit_dist[0][x] = x

# Recurrence Relation
for y in range(1, len(A) + 1):
    for x in range(1, len(B) + 1):
        # When the previous characters are equal,
        if A[y - 1] == B[x - 1]:
            # There's no need to change
            edit_dist[y][x] = edit_dist[y - 1][x - 1]
        else:
            # min(addition, deletion, and replacement) + 1
            edit_dist[y][x] = min(edit_dist[y - 1][x], edit_dist[y][x - 1], edit_dist[y - 1][x - 1]) + 1

print(edit_dist[len(A)][len(B)])

"""
abc
bcd
"""  # 2
