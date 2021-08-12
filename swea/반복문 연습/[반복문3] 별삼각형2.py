from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def star_triangle(length, shape):
    if shape == 1:
        half = length // 2
        for n in range(length):
            # 가운데 행을 중심으로 대칭
            # 이때 행 번호는 length를 2로 나눈 것보다 커짐
            if n > half:
                # length를 2로 몫만 가져오고, 다시 2를 곱하면 가운데
                # 가운데에서 현재 위치를 빼면 대칭되는 곳이 나옴
                n = half * 2 - n
            print("*" * (n + 1))
    elif shape == 2:
        half = length // 2
        for n in range(length):
            if n > half:
                n = half * 2 - n
            print(" " * (half - n), end="")
            print("*" * (n + 1))
    elif shape == 3:
        half = length // 2
        for n in range(length):
            if n > half:
                n = half * 2 - n
            print(" " * n, end="")
            print("*" * (length - 2 * n), end="")
            print(" " * n)
    elif shape == 4:
        half = length // 2
        for n in range(0, half):
            print(" " * n, end="")
            print("*" * (half + 1 - n))
        for n in range(half, length):
            print(" " * half, end="")
            print("*" * (n + 1 - half))
    else:
        pass

T = int(input())
for test_case in range(1, T + 1):
    print("#{}".format(test_case))
    length, shape = map(int, input().split())
    star_triangle(length, shape)