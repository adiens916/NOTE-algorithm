"""
아이디어: dmaolon00.tistory.com/entry/이코테Python-편집-거리-다이나믹-프로그래밍
"""


def count_min_edit_num(a: str, b: str) -> int:
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    for row in range(len(a) + 1):
        table[row][0] = row
    for col in range(len(b) + 1):
        table[0][col] = col

    for row in range(1, len(a) + 1):
        for col in range(1, len(b) + 1):
            if a[row - 1] == b[col - 1]:
                table[row][col] = table[row - 1][col - 1]
            else:
                prev_add = table[row][col - 1]
                prev_del = table[row - 1][col]
                prev_rep = table[row - 1][col - 1]
                table[row][col] = min(prev_add, prev_del, prev_rep) + 1

    return table[len(a)][len(b)]


A = input()
B = input()
print(count_min_edit_num(A, B))
