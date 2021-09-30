from pathlib import Path
import sys


parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
# input = sys.stdin.readline


"""
0. 배열 속에 숨은 숫자 파악하기 (핵심)
1. 숫자들로부터 암호 코드 만들어내기
2. 암호 코드가 정상인지 검증
3. 정상 코드의 자릿수 합 출력

0. 숨은 숫자 파악
+ 0과 1로만 이루어짐 => 이진수와 시프트 연산 활용
- 7자리가 하나의 숫자로 매핑 => 딕셔너리 활용
- 동일한 숫자가 여러 줄 반복 => 한 줄만 확인해도 됨
- 모두 맨 뒤에 1이 있음 => 맨 뒤에서부터 확인하면 찾기 쉬움
"""

def is_verified_cipher(cipher):
    odd_digit_sum = sum(cipher[0:7:2])
    even_digit_sum = sum(cipher[1:7:2])
    number = odd_digit_sum * 3 + even_digit_sum + cipher[7]
    return number % 10 == 0


# 각 숫자 암호
number_codes = {
    int('0001101', 2): 0,
    int('0011001', 2): 1,
    int('0010011', 2): 2,
    int('0111101', 2): 3,
    int('0100011', 2): 4,
    int('0110001', 2): 5,
    int('0101111', 2): 6,
    int('0111011', 2): 7,
    int('0110111', 2): 8,
    int('0001011', 2): 9
}


T = int(input())
for test_case in range(1, T + 1):
    print('#{}'.format(test_case), end=' ')

    N, M = map(int, input().split())
    # NOTE: 전부 이진수로 바꿔 받으면 오래 걸림. 
    # -> 필요할 때마다 바꾸는 걸로.
    arr = [input() for _ in range(N)]

    # 암호 코드 배열 & 몇 번째 자리에 넣을지 알려 줄 인덱스
    cipher = [0] * 8
    index = 7

    for row in arr:
        # 줄에 1이 하나도 없으면 넘김
        if '1' not in row:
            continue

        # 맨 뒤 0들을 지우고 이진수로 바꾸기
        row = int(row.rstrip('0'), 2)
        
        # 숫자가 8개 있으므로, 8번 반복
        for _ in range(8):
            # 맨 뒤 7개의 비트가 숫자의 키 값이 됨
            # => 1111111과 AND 연산하면 구할 수 있음
            number = number_codes[row & 0b1111111]
            
            # 해당 숫자를 암호 코드 마지막부터 채워넣기
            cipher[index] = number
            # 암호 코드 채울 자리를 한 칸 당김
            index -= 1
            # 다음 숫자를 가져오기 위해 7 비트 버림
            row >>= 7
    
        # 만든 암호 코드를 검증하기
        if is_verified_cipher(cipher):
            # 검증된 경우에만 합 출력
            print(sum(cipher))
        else:
            print(0)
        
        # 다른 행들은 둘러보지 않아도 되므로 반복문 나가기
        break
