import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


import tracemalloc

tracemalloc.start()


class Set:
    def __init__(self, size: int) -> None:
        self.size = size
        self.set = [False] * (size + 1)

    def add(self, elem: int) -> None:
        if self.set[elem]:
            return
        self.set[elem] = True

    def remove(self, elem: int) -> None:
        if not self.set[elem]:
            return
        self.set[elem] = False

    def check(self, elem: int) -> int:
        if self.set[elem]:
            return 1
        else:
            return 0

    def toggle(self, elem: int) -> None:
        if self.set[elem]:
            self.set[elem] = False
        else:
            self.set[elem] = True

    def all(self) -> None:
        for i in range(1, self.size + 1):
            self.set[i] = True

    def empty(self) -> None:
        for i in range(1, self.size + 1):
            self.set[i] = False


M = int(input())
small_set = Set(M)

size_1, peak_1 = tracemalloc.get_traced_memory()
print(f"{size_1=}, {peak_1=}")

for i in range(M):
    inputs = input().split()
    command = inputs[0]
    argument = int(inputs[1]) if len(inputs) > 1 else None

    if command == "add":
        small_set.add(argument)
    elif command == "remove":
        small_set.remove(argument)
    elif command == "check":
        print(small_set.check(argument))
    elif command == "toggle":
        small_set.toggle(argument)
    elif command == "all":
        small_set.all()
    elif command == "empty":
        small_set.empty()

    # size, peak = tracemalloc.get_traced_memory()
    # print(f"size_{i+2}={size}, peak_{i+2}={peak}")
