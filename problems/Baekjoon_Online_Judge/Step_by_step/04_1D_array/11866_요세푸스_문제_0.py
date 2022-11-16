import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    result = josephus_sequence(N, K)
    print(f"<{', '.join(result)}>")


def josephus_sequence(N: int, K: int):
    answer = []
    nums = [str(i) for i in range(1, N + 1)]
    index = 0
    count = 1

    while nums:
        if count < K:
            index += 1
            count += 1
        else:
            num = nums.pop(index)
            answer.append(num)

            N -= 1
            count = 1

        if index > N - 1:
            index = 0

    return answer


main()
