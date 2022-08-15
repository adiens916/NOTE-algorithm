import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


def eratosthenes_sieve(max_num: int):
    # 1로 초기화
    prime_table = [1] * (max_num + 1)
    prime_table[1] = 0

    # 범위는 제곱근까지
    sqrt = int(max_num ** 0.5)
    for i in range(2, sqrt + 1):
        # 소구가 아닌 수들의 배수들 역시 소수가 아니므로 스킵
        if prime_table[i] == 0:
            continue

        c = 2
        while c * i <= max_num:
            # 배수들의 인덱스는 0으로 채움
            prime_table[c * i] = 0
            c += 1
    return prime_table


M, N = map(int, input().split())
prime_table = eratosthenes_sieve(N)
primes = [x for x in range(M, N + 1) if prime_table[x]]
print(*primes, sep='\n')
