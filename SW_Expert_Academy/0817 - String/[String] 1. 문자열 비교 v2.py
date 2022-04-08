from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def make_push_table(str):
    """
    뒤에서부터 문자를 비교해, 얼마만큼 밀어줘야 하는지를 테이블로 준비
    이때 문자열에 포함된 문자면 해당 문자를 기점으로 위치를 조율해줘야 함.

    예를 들어 TRUST와 TOOTH의 경우, 끝의 T를 맞추기 위해 한 칸만 밀면 됨.
    TRUST -> TRUS'T'
    TOOTH ->  TOO'T'H

    이러면 적어도 한 글자 이상은 같고, 나머지 자리만 비교하면 되니까
    서로 일치할 가능성이 올라감.
    """

    table = {}
    length = len(str)

    # 각 문자를 끝에서 센 만큼 밀어줘야 함.
    # 이때 중복되는 글자는 뒤에 오는 쪽이 기준이 되어야 함.
    # 그래야 조금 밀어서 확인해볼 수 있으니까.
    # -> 앞에서부터 하되, 뒤에 오는 글자로 덮어씀
    for i in range(length - 1):
        table[str[i]] = (length - 1) - i
    
    # 마지막 H는 0이 아니라 5만큼 밀어줘야 함.
    # TRHTH와 TOOTH의 경우, 해당 기준에선 같은 게 나올 수 없으므로 아예 밀어줌.
    table[str[length - 1]] = length

    return table

def find_pattern(text, pattern):
    """
    Boyer Moore Horspool 알고리즘
    참고: https://www.youtube.com/watch?v=PHXAOKQk2dw&t=143s
    """

    push_table = make_push_table(pattern)
    text_len = len(text)
    pattern_len = len(pattern)

    # 초기 위치
    t = pattern_len - 1

    # 뒤에서부터 비교하니까, 텍스트 맨 뒤까지 가야 함
    while t < text_len:
        for i in range(pattern_len):
            # 뒤에서부터 문자 비교
            if text[t - i] != pattern[pattern_len - 1 - i]:
                # 문자가 서로 다른 경우 밀어줌
                if text[t] in push_table:
                    offset = push_table[text[t]]
                else:
                    offset = pattern_len
                t += offset
                break
        # 문자가 전부 같은 경우 패턴 시작 위치를 반환
        else:
            return t - pattern_len + 1

    # 패턴을 못 찾은 경우 -1을 반환
    return -1


T = int(input())
for test_case in range(1, T + 1):
    pattern = input().rstrip()
    text = input().rstrip()
    position = find_pattern(text, pattern)

#    result = 1 if position > -1 else 0
    print("#{} {}".format(test_case, position))
