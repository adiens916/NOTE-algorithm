def main():
    n = int(input())
    triangle = [list(map(int, input().split())) for _ in range(n)]
    print(max_integer_triangle(triangle))


def max_integer_triangle(triangle: list[list[int]]) -> int:
    n = len(triangle)
    # 두 번째 행부터 갱신
    for row in range(1, n):
        for col in range(row + 1):
            # 좌측 윗행에 있던 값 가져오기
            if col - 1 >= 0:
                left_up = triangle[row - 1][col - 1]
            else:
                left_up = 0

            # 우측 윗행에 있던 값 가져오기
            if col <= row - 1:
                right_up = triangle[row - 1][col]
            else:
                right_up = 0

            # 두 값 중 최댓값을 골라, 현재 요소에 더해 최댓값 만들기
            triangle[row][col] += max(left_up, right_up)

    # 마지막 행에서 가장 큰 숫자 반환
    answer = max(triangle[n - 1])
    return answer


main()

"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""
