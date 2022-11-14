import sys
from pathlib import Path

input_file = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_file)
input = sys.stdin.readline


def main():
    N = int(input())
    coords = [list(map(int, input().split())) for _ in range(N)]

    coords.sort()

    for x, y in coords:
        print(x, y)


main()
