from pathlib import Path
import sys


parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
# input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    print('#{}'.format(test_case), end=' ')

    decimal = input().lstrip('0.')
    integer = int(decimal)
    digits = len(decimal)
    binary_float = []
    
    while True: 
        #if integer % (10 ** digits) == 0:
        if integer == 0:
            print(*binary_float, sep='')
            break

        if len(binary_float) > 12:
            print('overflow')
            break 
        
        integer *= 2
        if integer >= (10 ** digits):
            binary_float.append(1)
        else:
            binary_float.append(0)

        integer %= (10 ** digits)
