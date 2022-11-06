import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
# 많은 개수를 입력받는 경우
# 반드시 sys.stdin.readline을 써야 한다.
# 참고; https://www.acmicpc.net/board/view/42763
input = sys.stdin.readline


def main():
    counting_sort(10000)


def counting_sort(max: int):
    counts = [0] * (max + 1)

    N = int(input())
    for _ in range(N):
        number = int(input())
        counts[number] += 1

    for i in range(1, max + 1):
        if counts[i]:
            # 문자열로 만들어서 출력하는 것도 메모리 소비함
            # => 그냥 출력하기
            for _ in range(counts[i]):
                print(i)


main()
