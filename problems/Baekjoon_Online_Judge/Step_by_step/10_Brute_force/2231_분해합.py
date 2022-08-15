import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline

'''
1. 각 자리수의 최대치는 9이므로,
2. 각 자리수 합의 최대치는 9 * (자리수 개수)
3. (현재 값 - 자리수 합 최대치) 값부터 생성자 찾기
'''

def get_decomposed_sum(n: int):
    d_sum = n
    d_sum += sum(map(int, list(str(n))))
    return d_sum


def get_generating_number(N: int):
    digits = len(str(N))

    for i in range(N - 9 * digits, N):
        if get_decomposed_sum(i) == N:
            return i
    
    # 없으면 0 반환
    return 0


N = int(input())
print(get_generating_number(N))


# 대조 검증
def brute_force(N: int):
    for i in range(1, N):
        if get_decomposed_sum(i) == N:
            print(i)
            break


# k = 0
# for i in range(990, 1030):
#     print(k)
#     k += 1
#     get_generating_number(i)
#     brute_force(i)