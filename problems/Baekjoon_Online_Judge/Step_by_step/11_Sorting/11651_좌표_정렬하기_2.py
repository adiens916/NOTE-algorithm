import sys
from pathlib import Path

input_file = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_file)
input = sys.stdin.readline


def main():
    N = int(input())
    coords = [input().rstrip() for _ in range(N)]
    coords.sort(key=lambda coord: weight_on_y(coord))
    print("\n".join(coords))


def weight_on_y(coord: str):
    x, y = coord.split()
    return int(y) + int(x) / 1000000


main()
