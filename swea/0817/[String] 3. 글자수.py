from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def make_dict(str):
    d = {}
    for char in str:
        d[char] = d.get(char, 0) + 1
    return d

def count_most_char(str1, str2):
    str2_dict = make_dict(str2)
    most_num = 0

    for char in str1:
        if char in str2_dict:
            if most_num < str2_dict[char]:
                most_num = str2_dict[char]
    
    return most_num

T = int(input())
for test_case in range(1, T + 1):
    str1 = input().rstrip()
    str2 = input().rstrip()
    count = count_most_char(str1, str2)
    print("#{} {}".format(test_case, count))