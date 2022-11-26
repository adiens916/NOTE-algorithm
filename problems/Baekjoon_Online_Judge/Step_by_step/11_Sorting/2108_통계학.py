import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


MAX_ABS = 4000


def main():
    N = int(input())
    numbers = [int(input()) for _ in range(N)]
    statistic = Statistic(numbers)

    print(statistic.avg())
    print(statistic.median())
    print(statistic.most())
    print(statistic.range())


class Statistic:
    def __init__(self, numbers: list[int]) -> None:
        self.numbers = numbers

    def avg(self) -> int:
        total_sum = 0
        for number in self.numbers:
            total_sum += number
        average = total_sum / len(self.numbers)

        rounded = (average + 0.5) * 10 // 10
        return int(rounded)

    def median(self) -> int:
        self.numbers.sort(reverse=True)
        middle = (len(self.numbers) + 1) // 2
        return self.numbers[middle - 1]

    def most(self) -> int:
        positive_counts = [0] * (MAX_ABS + 1)
        negative_counts = [0] * (MAX_ABS + 1)

        for number in self.numbers:
            if number >= 0:
                positive_counts[number] += 1
            else:
                negative_counts[number] += 1
        count = lambda x: positive_counts[x] if x >= 0 else negative_counts[x]

        unique_numbers = list(set(self.numbers))
        unique_numbers.sort(reverse=True)
        unique_numbers.sort(key=count)

        most = unique_numbers[-1]
        if len(unique_numbers) == 1:
            return most

        next_most = unique_numbers[-2]
        if count(most) > count(next_most):
            return most
        else:
            return next_most

    def range(self) -> int:
        return self.numbers[0] - self.numbers[-1]


main()
