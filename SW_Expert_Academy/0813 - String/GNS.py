from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


number_table = {
    "ZRO": 0, 
    "ONE": 1, 
    "TWO": 2, 
    "THR": 3, 
    "FOR": 4, 
    "FIV": 5, 
    "SIX": 6, 
    "SVN": 7, 
    "EGT": 8, 
    "NIN": 9
}

T = int(input())
for test_case in range(1, T + 1):
    # 문자로 된 숫자들을 넣을 리스트
    number_array = [[] for _ in range(10)]
    test_case, seq_num = input().split()
    sequence = list(input().split())

    # 문자열 중 각각의 문자로 된 숫자들에 대해
    for word in sequence:
        # 문자에 대응하는 숫자를 알아내고
        number = number_table[word]
        # 그 숫자를 인덱스로 삼아 각각의 리스트 끝에 추가
        number_array[number].append(word)
    
    print(test_case)
    # 먼저 10개 리스트 각각 안에 들어있는 수백 개의 문자들을 이어주고,
    # 그렇게 이어진 10개의 문자열들을 다시 하나의 문자열로 이어줌
    print(
        ' '.join(
            ' '.join(number) for number in number_array
        )
    )