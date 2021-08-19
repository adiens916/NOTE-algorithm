from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline



def length_without_duplicates(string):
    stack = []

    for char in string:
        # 스택이 비어있으면 그냥 추가
        if len(stack) == 0:
            stack.append(char)
        else:
            # 스택 맨 윗 글자와 같으면 짝이 맞음
            # -> 스택 위에 있는 것 제거
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
    
    return len(stack)
    

T = int(input())
for test_case in range(1, T + 1):
    string = input().rstrip()
    length = length_without_duplicates(string)
    print("#{} {}".format(test_case, length))
