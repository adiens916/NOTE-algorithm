from pathlib import Path
import sys


parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}/{file_name} input.txt")
# input = sys.stdin.readline


"""
1. 16진수 찾아내기 
    - 오른쪽부터 읽다가 0 아닌 것 계속 찾기 & 윗 행이 0인 것만
2. 16진수로부터 2진수 만들기
    - 직접 매핑 (int -> str)
    - 나중에 길이가 부족하면, 더 긴 쪽에 맞춰 앞에 0 붙여주기
3. 2진수로부터 숫자 만들기
    - 슬라이싱을 통해 1, 2, 3, ..., n칸 훑으며
    숫자 8개가 제대로 만들어질 때까지 무한반복
4. 숫자들로 암호코드 만들고, 정상인지 확인
    - 문자열 매핑
5. 정상이면 합 더하기
6. 모든 합 출력
"""

hex_table = {hex(i).upper()[-1]: f'{int(bin(i)[2:]):04}' for i in range(16)}

number_table = {
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
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    cipher_sum = 0

    for row in range(N):
        # 16진수 찾아내기
        # for col in range(M - 1, -1, -1):
        #     if arr[row][col] != '0':
        #         last = col
        #         break
        # else:
        #     continue
        row_middle = arr[row].rstrip('0')
        if row_middle == '':
            continue
        else:
            last = len(row_middle) - 1

        # 이미 있던 숫자는 넘김
        # FIXME: 위아래 같으면 무조건 넘어가게 해야 함...
        for col in range(last, -1, -1):
            if row == 0 or arr[row - 1][col] == '0':
                break
            else:
                while arr[row - 1][col] == arr[row][col]:
                    col -= 1
                    if col == 0:
                        break
                last = col
                break

        # 0 밖에 없으면 다음 행으로
        if arr[row][:last + 1].strip('0') == '':
            continue

        # 앞쪽에서부터 16진수 -> 2진수로 전부 변환            
        bin_string = ''
        for col in range(last + 1):
            bin_string += hex_table[arr[row][col]]
        
        # 2진수로부터 숫자 만들기
        last = len(bin_string) - 1
        while last >= 0:
            if bin_string[last] != '0':
                
                cipher = [0] * 8
                cipher_index = 7
                boldness = 1
                end = last
                start = end - 7 * boldness + 1
                
                while True:
                    if cipher_index < 0:
                        break
                    
                    for i in range(1, 9):
                        encoded_number = bin_string[start: end + 1]
                        encoded_number = encoded_number[: : boldness]
                        decoded_number = number_table.get(encoded_number, -1)
                        if decoded_number == -1:
                            boldness += 1
                            
                            cipher = [0] * 8
                            cipher_index = 7
                            end = last
                            start = end - 7 * boldness + 1
                            break
                        else:
                            cipher[cipher_index] = decoded_number
                            cipher_index -= 1
                            end = start - 1
                            start = end - 7 * boldness + 1

                if (sum(cipher[0:7:2]) * 3 + sum(cipher[1:8:2])) % 10 == 0:
                    cipher_sum += sum(cipher)
            
                last = start - 1
            
            else:
                last -= 1
    
    print(cipher_sum)
