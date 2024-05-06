def main():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        mines_1d = list(map(int, input().split()))

        # 2차원 배열로 바꾸기
        mines = get_2d_mines(mines_1d, n, m)

        # 최대 금 크기 계산
        max_gold = find_max_gold(mines, n, m)
        print(max_gold)


def get_2d_mines(mines: list[int], n: int, m: int) -> list[list[int]]:
    result = [[0] * m for _ in range(n)]
    for i in range(len(mines)):
        result[i // m][i % m] = mines[i]
    return result


def find_max_gold(mines: list[list[int]], n: int, m: int) -> int:
    max_mines = [[0] * m for _ in range(n)]
    # XXX: 현재 금 크기 복사
    for row in range(n):
        for col in range(m):
            max_mines[row][col] = mines[row][col]

    for col in range(1, m):
        for row in range(n):
            max_val = 0
            # XXX: 뒤에서 앞쪽에 있는 걸 계산해야 함
            # 앞에서 뒤로 계산하면 배열을 2개 써야 함. (최댓값 & 원래 값)
            x = col - 1
            for dy in (-1, 0, 1):
                y = row + dy
                # 범위 계산
                if not (0 <= y < n and 0 <= x < m):
                    continue

                # 앞 열에서 최대치 찾기
                max_val = max(max_val, max_mines[y][x])
            # 현재 값에 앞에서 찾은 최대치 더하기
            max_mines[row][col] += max_val

    # 마지막 열에서 가장 큰 것 찾기
    max_val = 0
    for row in range(n):
        max_val = max(max_val, max_mines[row][m - 1])

    return max_val


main()

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2 
"""
