import sys
from sys import stdin
input = stdin.readline

# https://www.acmicpc.net/source/42385263
def solution(open = open):
    che = [False, False, True, True] + [False, True] * 4998
    for i, is_prime in enumerate(che[3:int(10000 ** .5) + 1:2], start=1):
        if not is_prime:
            continue
        prime = i * 2 + 1
        che[prime * prime::2 * prime] = [False] * ((10000 - prime * prime) // (2 * prime) + 1)
    input = iter(open(0).read().split("\n")).__next__
    for _ in range(int(input())):
        n = int(input())
        if n == 4:
            print(2, 2)
        n2 = n // 2
        if n2 % 2 == 0:
            n2 -= 1
        for prime in range(n2, 0, -2):
            if che[prime] and che[n - prime]:
                print(prime, n - prime)
                break
solution()

# https://www.acmicpc.net/source/21325196
T = int(input())
answer = ""
result = [False, False, True] + [True, False] * 5000
for number in range(3, 101, 2):
    if result[number]:
        result[number*2::number] = [False] * len(result[number*2::number])

for tc in range(T):
    N = int(input())
    if N == 4:
        answer += "2 2\n"
        continue
    harf_N = N//2
    if not harf_N % 2:
        harf_N += 1
    for i in range(harf_N, N, 2):
        if result[i] and result[N-i]:
            answer += "{} {}".format(N - i, i) + "\n"
            break
print(answer, end="")

# https://www.acmicpc.net/source/18398164
ck = [ False, False ] + [ True ] * (10000 - 1)
for i in range(2, 10001):
    if ck[i] == False : continue
    for j in range(i * 2, 10001, i):
        ck[j] = False

for _ in range(int(input())):
    target = int(input())
    halfTarget = target // 2
    for i in range(halfTarget, 1, -1):
        if (ck[i] and ck[target - i]):
            print(f"{i} {target - i}")
            break

# https://www.acmicpc.net/source/15637300
# prime: 에라토스테네스의 체
limit = 10000
tf_prime = [False, False] + [True]*(limit-1)
for i in range(2, int(limit**0.5)+1):
    if tf_prime[i]:
        for j in range(i+i, limit+1, i):
            tf_prime[j] = False

# 골드바흐
n = int(sys.stdin.readline())
for _ in range(n):
    even = int(sys.stdin.readline())
    for j in range(even//2, even+1):
        if tf_prime[j] and tf_prime[even-j]:
            print('{} {}'.format(even-j, j))
            break