import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


# 값 입력
N = int(input())
numbers = list(map(int, input().split()))
# 주어진 수 중 최댓값까지만 소수 판별하기
max_num = max(numbers)

# 소수 판별하는 배열 생성
# 주어진 수 각각에 대해 소수 판별하면 반복되기 때문
primes = [1] * (max_num + 1)
primes[1] = 0

for i in range(2, max_num // 2 + 1):
    # 자기 자신은 소수에 포함시키고, 그 다음부터 계산
    c = 2
    while c * i <= max_num:
        primes[c * i] = 0
        c += 1

# 소수 개수들의 합을 구해 출력
count = sum([primes[i] for i in numbers])
print(count)
