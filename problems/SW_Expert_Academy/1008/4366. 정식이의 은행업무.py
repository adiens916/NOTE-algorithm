from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    binary = list(map(int, input().rstrip()))
    ternary = list(map(int, input().rstrip()))

    # 2진수 -> 10진수
    dec_from_bin = set()
    for i in range(len(binary)):
        # 한 자리 바꿈
        binary[i] ^= 1

        # 이진수 -> 십진수 변환 후 추가
        dec = 0
        for j in range(len(binary)):
            dec = dec * 2 + binary[j]
        dec_from_bin.add(dec)
        
        # 복구
        binary[i] ^= 1
   
    # 3진수 -> 10진수
    dec_from_tert = set()
    for i in range(len(ternary)):
        # 원본
        origin = ternary[i]
        for j in range(3):
            # 원본과 다른 자리로 바꾸기
            if ternary[i] != j:
                ternary[i] = j

                # 삼진수 -> 십진수 변환 후 추가
                dec = 0
                for k in range(len(ternary)):
                    dec = dec * 3 + ternary[k]
                dec_from_tert.add(dec)
                
                # 복구
                ternary[i] = origin

    # 공통 <- 교집합
    answer = dec_from_bin.intersection(dec_from_tert)

    print('#{} {}'.format(test_case, answer.pop()))
