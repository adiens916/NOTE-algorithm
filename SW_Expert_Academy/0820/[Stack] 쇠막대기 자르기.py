from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def split_by_stack(string):
    """
    어떤 중심에 오면 이벤트 발생 -> 스택을 이용

    (면 일단 스택에 추가
    ()일 때, 스택에 담겨있던 것만큼 잘림
    그 뒤에 나오는 ) 개수만큼 잘린 막대기 추가
    """
    count = 0
    stack = []
    prev = ""

    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            # 바로 이전 값이 (일 때만 레이저 출력
            if stack and prev == "(":
                stack.pop()
                # 막대는 현재 들어있는 괄호 개수만큼
                count += len(stack)
            # 이전 값이 (가 아니면 막대 끝
            else:
                stack.pop()
                # 하나의 막대 끝 -> 한 개만 추가
                # 나머지는 아직 더 처리되어야 하니까 그대로 놔둠
                count += 1

        # stack 만으로는 바로 이전 글자 판별 불가
        # 왜냐하면 짝을 맞춰 사라지기 때문
        # -> 따로 변수를 두고 매번 체크
        prev = char

    return count


T = int(input())
for test_case in range(1, T + 1):
    string = input()
    count = split_by_stack(string)
    print("#{} {}".format(test_case, count))
