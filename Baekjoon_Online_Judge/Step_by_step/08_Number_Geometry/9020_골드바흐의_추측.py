import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


def eratosthenes_sieve(max_num: int):
    prime_table = [False, False] + [True] * (max_num - 1)

    sqrt = int(max_num ** 0.5)
    for i in range(2, sqrt + 1):
        if prime_table[i]:
            for j in range(i * i, max_num + 1, i):
                prime_table[j] = False
    
    return prime_table


def goldbach_partition(num: int):
    global prime_table

    for i in range(num // 2, 1, -1):
        if prime_table[i] and prime_table[num - i]:
            return [i, num - i]


numbers = list(map(int, list(sys.stdin)[1:]))
max_num = max(numbers)
prime_table = eratosthenes_sieve(max_num)

for number in numbers:
    print(*goldbach_partition(number))