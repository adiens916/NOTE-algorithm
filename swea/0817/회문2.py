from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline



def find_longest_palindrome_in_row(matrix):
    # 가장 먼 곳에서부터 가까이 오면서 회문 판별하기
    longest_len = 1

    for row in range(N):
        for col in range(N):
            # 먼 곳에서부터 오면서
            for end in range(N - 1, col, -1):
                # 처음과 같은 걸 찾는다.
                if matrix[row][col] == matrix[row][end]:
                    length = end - col + 1
                    # 구간이 현재 최대 길이보다 짧다면 건너띈다.
                    if length < longest_len:
                        break
                    # 처음과 같은 문자를 기점으로 점점 좁혀오고,
                    for diff in range(length // 2):
                        # 중간에 틀린 게 있으면 종료 후, 다시 처음과 같은 걸 찾는다.
                        if matrix[row][col + diff] != matrix[row][end - diff]:
                            break
                    else:
                        longest_len = length if length > longest_len else longest_len
            # 처음과 같아지면 다음 글자로 완전히 넘어간다.
    
    return longest_len


def find_longest_palindrome_in_col(matrix):
    # 가장 먼 곳에서부터 가까이 오면서 회문 판별하기
    longest_len = 1

    # 먼 곳에서부터 오면서
    for col in range(N):
        for row in range(N):
            for end in range(N - 1, row, -1):
                # 처음과 같은 걸 찾는다.
                if matrix[row][col] == matrix[end][col]:
                    length = end - row + 1
                    if length < longest_len:
                        break
                    # 그 애를 기점으로 점점 좁혀오고,
                    for diff in range(length // 2):
                        # 중간에 틀린 게 있으면 종료 후, 다시 처음과 같은 걸 찾는다.
                        if matrix[row + diff][col] != matrix[end - diff][col]:
                            break
                    else:
                        longest_len = length if length > longest_len else longest_len
            # 처음과 같아지면 다음 글자로 완전히 넘어간다.

    return longest_len

N = 100

T = 10
for test_case in range(1, T + 1):
    input()
    matrix = [list(input()) for _ in range(N)]
    longest_in_row = find_longest_palindrome_in_row(matrix)
    longest_in_col = find_longest_palindrome_in_col(matrix)
    
    if longest_in_row > longest_in_col:
        print("#{} {}".format(test_case, longest_in_row))
    else:
        print("#{} {}".format(test_case, longest_in_col))

