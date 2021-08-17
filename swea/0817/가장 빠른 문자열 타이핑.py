from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def count_least_typing(string, word):
    string_len = len(string)
    word_len = len(word)
    count = 0

    base = 0
    while base < string_len:
        for offset in range(word_len):
            # 비교하려는데 길이가 모자라는 경우
            if base + offset >= string_len:
                # 그냥 남은 길이는 일일이 타이핑
                count += offset
                base += offset
                break

            # 길이 비교
            if string[base + offset] != word[offset]:
                # FIXME: 처음부터 틀렸을 때 offset이 0이라 안 밀려남
                # -> 처음을 따로 처리해주기
                if offset == 0:
                    offset = 1
                count += offset
                base += offset
                break

        # 전부 같은 경우 1만큼 증가
        else:
            count += 1
            base += word_len
    
    return count


T = int(input())
for test_case in range(1, T + 1):
    string, word = input().split()
    count = count_least_typing(string, word)
    print("#{} {}".format(test_case, count))