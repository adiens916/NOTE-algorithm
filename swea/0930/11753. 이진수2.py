from pathlib import Path
import sys


parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
# input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')

    decimal = input().lstrip('0.')
    digits = len(decimal)
    decimal = int(decimal)
    bin_decimal = ''

    while decimal % (10 ** digits) != 0:
        decimal *= 2
        if decimal >= (10 ** digits):
            bin_decimal += '1'
        else:
            bin_decimal += '0'

        decimal %= (10 ** digits)
        if len(bin_decimal) > 12:
            print('overflow')
            break 
    else:
        print(bin_decimal)
