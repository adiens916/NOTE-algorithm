import sys
import bisect
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


def eratosthenes_sieve(max_num: int):
    # 배열을 참으로 초기화 (전부 소수라고 가정)
    prime_table = [True] * (max_num + 1)
    # 0과 1은 소수 아님
    prime_table[:2] = [False, False]

    # 약수의 범위는 제곱근까지
    sqrt = int(max_num ** 0.5)
    for i in range(2, sqrt + 1):
        # 약수가 소수인 경우,
        if prime_table[i]:
            # 배수들은 소수가 아님
            for j in range(i * i, max_num + 1, i):
                prime_table[j] = False

    return prime_table


inputs = list(sys.stdin)[:-1]
numbers = list(map(int, inputs))
max_num = max(numbers)
prime_table = eratosthenes_sieve(2 * max_num)
primes = [i for i in range(2 * max_num + 1) if prime_table[i]]

for number in numbers:
    start = bisect.bisect_right(primes, number)
    end = bisect.bisect_right(primes, 2 * number)
    print(end - start)

# for number in numbers:
#     print(sum([prime_table[x] for x in range(number + 1, 2 * number + 1)]))

"""
1
4
3
21
135
1033
8392
"""