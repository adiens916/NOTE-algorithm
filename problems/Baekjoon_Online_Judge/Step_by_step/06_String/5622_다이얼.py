"""https://www.acmicpc.net/problem/5622"""

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


def make_char_num_dict():
    """
    전화번호의 문자와 해당하는 숫자를 연결한 딕셔너리 반환
    """
    char_num_dict = {}
    
    def add(start_char, end_char, number):
        for char_idx in range(ord(start_char), ord(end_char) + 1):
            char_num_dict[chr(char_idx)] = number
    
    # 알파벳 A부터 Z까지 매핑
    add('A', 'C', 2)
    add('D', 'F', 3)
    add('G', 'I', 4)
    add('J', 'L', 5)
    add('M', 'O', 6)
    add('P', 'S', 7)
    add('T', 'V', 8)
    add('W', 'Z', 9)
    
    # 구간별로 자르는 방법
    # for char_idx in range(ord('A'), ord('R') + 1):
    #     number = (char_idx - ord('A')) // 3 + 2
    #     char_num_dict[chr(char_idx)] = number
    # char_num_dict['S'] = 7
    # for char_idx in range(ord('T'), ord('Y') + 1):
    #     number = (char_idx - ord('T')) // 3 + 8
    #     char_num_dict[chr(char_idx)] = number
    # char_num_dict['Z'] = 9

    return char_num_dict


total_time = 0
char_num_dict = make_char_num_dict()

string = input().rstrip()
for char in string:
    # 각 문자에 해당하는 숫자를 찾고, 걸리는 시간 더하기
    total_time += char_num_dict[char] + 1

print(total_time)