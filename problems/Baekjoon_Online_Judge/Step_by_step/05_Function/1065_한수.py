import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


# 한수 여부 파악
def is_arithmetic_sequence(x: int):
    # 두 자릿수인 경우에는 무조건 등차수열
    if x < 100:
        return True
    
    # 1. 자릿수마다 쪼개기
    numbers = list(map(int, list(str(x))))
    # 2. 기준이 되는 등차를 구하기
    diff = numbers[1] - numbers[0]
    # 3. 다음 자릿수부터 기준 등차와 비교하기
    for digit in range(1, len(numbers) - 1):
        if numbers[digit + 1] - numbers[digit] != diff:
            # 다르면 등차수열 아님
            return False
    # 등차가 전부 같았으면 등차수열
    return True


N = int(input())
count = 0
for num in range(1, N + 1):
    if is_arithmetic_sequence(num):
        count += 1
print(count)