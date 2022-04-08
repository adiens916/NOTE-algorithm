from pathlib import Path
import sys


parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
0. 배열 속에 숨은 숫자 파악하기 (핵심★)
1. 숫자들로부터 암호 코드 만들어내기
2. 암호 코드가 정상인지 검증
3. 정상 코드의 자릿수 합 출력

0. 숨은 숫자 파악
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
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


T = int(input())
for test_case in range(1, T + 1):
    print('#{}'.format(test_case), end=' ')

    N, M = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]

    # 암호 코드 배열 & 몇 번째 자리에 넣을지 알려 줄 인덱스
    cipher = [0] * 8
    index = 7

    for row in arr:
        # 1이 없는 줄 = 암호 코드가 없는 줄은 넘기기
        if '1' not in row:
            continue

        # 뒤에서부터 1 찾기
        last = M - 1
        while row[last] != '1':
            last -= 1
        
        # 숫자가 8개 있으므로, 8번 반복
        for _ in range(8):
            # 앞으로 7칸 가서 이번 숫자 시작 지점으로 가기
            start = last - 6
            # 7칸에 해당하는 숫자를 딕셔너리에 넣어 알아내기
            number = number_codes[row[start : last + 1]]
            
            # 해당 숫자를 암호 코드 마지막부터 채워넣기
            cipher[index] = number
            # 암호 코드 채울 자리를 한 칸 당기고, 다음 숫자로 이동
            index -= 1
            last = start - 1
    
        # 만든 암호 코드를 검증하기
        if is_verified_cipher(cipher):
            # 검증된 경우에만 합 출력
            print(sum(cipher))
        else:
            print(0)
        
        # 다른 행들은 둘러보지 않아도 되므로 반복문 나가기
        break
