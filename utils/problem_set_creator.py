"""
문제 번호와 이름을 입력하면, 소스 코드와 입출력 텍스트 만들어줌.

사용법
1. 첫 줄에 문제 번호를 적고
2. 그 다음 줄에 문제 이름을 적어준다.

입력 예시
1234
아기 상어
5678
아닛?!

결과 예시
1234_아기_상어.py
5678_아닛?!.py

"""

import os
from pathlib import Path
from datetime import date


# input.txt를 읽어오기 위해 소스 첫 부분에 써주는 코드
INPUT_TEMPLATE = '''\
from pathlib import Path
directory = Path(__file__).parent
file_name = Path(__file__).stem
input_text = f"{directory}\{file_name}_input.txt"

import sys
sys.stdin = open(input_text)
input = sys.stdin.readline'''


# 오늘 날짜에 맞는 폴더를 만듦
def make_directory_for_today():
    # 오늘 날짜
    today = date.today()
    dir_name = f"{today.month:02}{today.day:02}"

    # 새로운 폴더의 경로
    problem_set_dir = f"{Path(__file__).parent}\{dir_name}"

    # 폴더가 이미 있으면 오류, 없으면 새로 만들기
    try: 
        if not os.path.exists(problem_set_dir):
            os.makedirs(problem_set_dir)
    except OSError as e:
        print(e)

    # 새로운 폴더 경로 반환
    return problem_set_dir


# 문제 제목에서 괄호 이후만 가져오는 함수
def extract_problem_name(line: str, blank_to_underscore=False):
    # 공백을 밑줄로 바꾸기
    if blank_to_underscore:
        line = line.replace(' ', '_')

    # 특수문자를 바꾸기
    for sp, no_sp in (('?', '？'), ('!', '！')):
        if sp in line:
            line = line.replace(sp, no_sp)

    if ']' in line:
        # 괄호를 기준으로 나누고, 뒤에 있는 걸 가져옴
        name = line.split(']')[1]
        # 공백을 제거하고 반환
        return name.strip()
    else:
        return line.strip()


def create_problem_set(problem_file, in_folder=True):
    if in_folder:
        target_dir = make_directory_for_today()
    else:
        target_dir = Path(__file__).parent

    text = open(f"{Path(__file__).parent}\{problem_file}", "rt", encoding='UTF8')
    is_num_before = False
    for line in text:
        # 문제 번호 확인
        if "0" <= line[0] <= "9" and not is_num_before:
            problem_num = line.split()[0]
            is_num_before = True
        
        # 문제 번호 다음에 문제 이름이 오는데, 그 이름을 바탕으로 파일 생성
        elif is_num_before:
            # python 파일 생성
            file_name = problem_num + '_' + extract_problem_name(line, True)
            f = open(f"{target_dir}\{file_name}.py", "w", encoding="UTF8")
            
            # 파일 처음에 input 읽어오는 문구 작성
            f.write(INPUT_TEMPLATE)
            f.close()

            # input txt 생성
            f = open(f"{target_dir}\{file_name}_input.txt", "w", encoding="UTF8")
            f.close()

            # output txt 생성
            # f = open(f"{target_dir}\{file_name}_output.txt", "w", encoding="UTF8")
            # f.close()


            is_num_before = False
        
    text.close()


if __name__ == "__main__":
    create_problem_set("problem_info.txt", in_folder=False)