from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
# input = sys.stdin.readline


def find_palindrome_with_length(matrix, string_length):
    matrix_length = len(matrix)

    for row in range(matrix_length):
        for col in range(matrix_length - string_length + 1):
            # FIXME: 차라리 offset 값을 col에 더해나가기
            for diff in range(string_length // 2):
                if matrix[row][col + diff] != matrix[row][col + string_length - 1 - diff]:
                    break
            else:
                return "".join(matrix[row][col : col + string_length])

    for col in range(matrix_length):
        for row in range(matrix_length - string_length + 1):
            for diff in range(string_length // 2):
                if matrix[row + diff][col] != matrix[row + string_length - 1 - diff][col]:
                    break
            else:
                string = [matrix[y][col] for y in range(row, row + string_length)]
                return "".join(string)


T = int(input())
for test_case in range(1, T + 1):
    matrix_length, string_length = map(int, input().split())
    matrix = [list(input()) for _ in range(matrix_length)]
    
    string = find_palindrome_with_length(matrix, string_length)
    print("#{} {}".format(test_case, string))
