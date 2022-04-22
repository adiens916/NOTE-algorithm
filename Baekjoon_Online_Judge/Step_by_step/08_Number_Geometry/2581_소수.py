import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


def get_prime_table(max_num):
    prime_table = [1] * (max_num + 1)
    prime_table[1] = 0
    for i in range(2, max_num + 1):
        c = 2
        while c * i <= max_num:
            prime_table[c * i] = 0
            c += 1    
    return prime_table


M = int(input())
N = int(input())

# 소수 테이블을 구한 후, 이에 기반하여 소수 판별
prime_table = get_prime_table(N)
primes = [i for i in range(M, N + 1) if prime_table[i]]

# 소수인 것을 모두 찾아 합과 최솟값 출력
if primes:
    print(sum(primes))
    print(primes[0])
# 소수가 없으면 -1 출력
else:
    print(-1)
