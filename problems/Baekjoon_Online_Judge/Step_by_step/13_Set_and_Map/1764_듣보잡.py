import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    not_heard = [input().strip() for _ in range(N)]
    not_seen = [input().strip() for _ in range(M)]
    both = []

    hash_table = HashTable(not_heard)
    for not_seen_name in not_seen:
        index = hash_table.get_index(not_seen_name)
        if index == -1 or index >= N:
            continue

        not_heard_name = not_heard[index]
        if not_heard_name == not_seen_name:
            both.append(not_seen_name)

    both.sort()
    print(len(both))
    print("\n".join(both))


class HashTable:
    def __init__(self, source: list[str]) -> None:
        self.table_max = 500000 * 2 + 9
        self.table = [None] * self.table_max

        for i in range(len(source)):
            hash_value = self.get_hash(source[i])
            self.table[hash_value] = i

    def get_hash(self, string: str) -> int:
        hash_value = 0
        for i in range(len(string)):
            hash_value += ord(string[i]) * 7**i
        return hash_value % self.table_max

    def get_index(self, string: str) -> int:
        hash_value = self.get_hash(string)
        index = self.table[hash_value]
        return index if index != None else -1


main()
