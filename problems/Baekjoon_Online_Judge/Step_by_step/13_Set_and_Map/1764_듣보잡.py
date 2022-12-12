import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    not_heard = set([input().strip() for _ in range(N)])
    not_seen = set([input().strip() for _ in range(M)])
    both = not_heard.intersection(not_seen)

    both = sorted(list(both))
    print(len(both))
    print("\n".join(both))


main()
