T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    mines = [[0] * M for _ in range(N)]
    for row in range(N):
        for col in range(M):
            mines[row][col] = arr[row * M + col]
    # print(mines)

    for col in range(M - 2, -1, -1):
        for row in range(N):
            if row == 0:
                up = 0
            else:
                up = mines[row - 1][col + 1]

            right = mines[row][col + 1]

            if row == N - 1:
                down = 0
            else:
                down = mines[row + 1][col + 1]

            mines[row][col] += max(up, right, down)

    first_cols = [mines[row][0] for row in range(N)]
    print(max(first_cols))

"""
나는 우측에서부터 오게끔 풀었지만, 풀이에서는 좌측에서부터 감.
차이점이라 한다면, 다른 문제들은 경우에 따라 중간 경로가 달라짐.
그러나 이 문제는 이미 지난 경로가 답에 포함될 가능성이 없음.
그러므로 좌측에서부터 풀어도 되는 것이다.
"""