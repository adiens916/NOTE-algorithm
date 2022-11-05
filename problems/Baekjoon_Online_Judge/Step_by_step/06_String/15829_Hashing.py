from pathlib import Path

parent = Path(__file__).parent
filename = Path(__file__).stem

import sys

sys.stdin = open(f"{parent}/{filename}_input.txt")
input = sys.stdin.readline

####################


def char_to_num(char: str) -> int:
    return ord(char) - ord("a") + 1


def hash_by_power(string: str):
    r = 31
    M = 1234567891

    sequence_sum = 0
    for i in range(len(string)):
        sequence_sum += char_to_num(string[i]) * (r**i)

    H = sequence_sum % M
    return H


L = int(input())
string = input().strip()
print(hash_by_power(string))
