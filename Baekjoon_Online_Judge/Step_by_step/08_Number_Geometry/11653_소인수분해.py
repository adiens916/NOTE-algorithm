import sys
import math
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


def factorize(n: int):
    # 소인수분해 과정 중간에 나오는 합성수들을
    # composites라는 리스트에 담음.

    # 배열 크기가 24인 이유:
    # 최대 범위가 10^7일 때, 합성수의 개수는 최대 24개
    # 왜냐하면 가장 작은 소수인 2로만 구성했을 때 24개이기 때문.
    # 2^10 (1024) * 2^10 * 2^4 > 10^7
    composites = [0] * 24
    i = 0
    composites[i] = n

    # 소인수분해 결과들 담는 리스트
    factors = [0] * 24
    j = 0

    # 합성수가 하나라도 있는 한 반복
    while i >= 0:
        # 소인수분해는 제곱근 이하로만 가능
        sqrt_floor = math.floor(math.sqrt(composites[i]))
        # 나누는 수가 1보다 큰 경우
        k = 0
        while sqrt_floor - k > 1:
            # 나눠떨어지는지 확인
            if composites[i] % (sqrt_floor - k) == 0:
                # 나눠떨어진 수를 현재 합성수 위치에 덮어씌움
                composites[i] = composites[i] // (sqrt_floor - k)
                # 나누는 수를 다음 합성수로 넣음
                i += 1
                composites[i] = sqrt_floor - k
                break
            k += 1
        
        # 나눠떨어지지 않은 경우, 소수임
        if sqrt_floor - k == 1:
            # 해당 수를 소수로 옮기고, 인덱스 조정
            factors[j] = composites[i]
            i -= 1
            j += 1
    
    # 소수들을 오름차순으로 정렬해서 반환
    return sorted([x for x in factors if x > 0])


N = int(input())
if N != 1:
    print(*factorize(N), sep='\n')
