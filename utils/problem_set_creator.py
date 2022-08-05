from pathlib import Path

from utils_module.directory_creator import DirectoryCreator
from utils_module.string_editor import StringEditor
from utils_module.file_creator import FileCreator
from utils_module.file_editor import FileEditor


class ProblemTemplateCreator:
    """
    텍스트 파일에 문제 번호와 이름을 입력하면, 
    해당 이름을 갖는 소스 파일과 입출력 텍스트를 생성.

    [입력 예시]
    1234
    아기 상어
    5678
    아닛?!

    [결과 예시]
    1234_아기_상어.py
    1234_아기_상어_input.txt
    5678_아닛?!.py
    5678_아닛?!_input.txt
    """

    problem_text = None
    problem_numbers_and_names = []
    created_directory = Path(__file__).parent

    def __init__(self, problem_text: str, for_today=False) -> None:
        self.problem_text = open(f"{Path(__file__).parent}\{problem_text}", encoding='UTF8')
        if for_today:
            self.__change_created_directory()

    def __change_created_directory(self):
        directory_creator = DirectoryCreator(self.created_directory)
        directory_creator.create_as_today()
        self.created_directory = directory_creator.created_directory

    def __call__(self) -> None:
        self.extract_numbers_and_names()
        self.__replace_special_character()
        self.__replace_space_to_underscore()
        self.__create()
    
    def extract_numbers_and_names(self) -> None:
        problem_text_lines = list(self.problem_text)
        numbers = list(map(str.strip, problem_text_lines[::2]))
        names = list(map(str.strip, problem_text_lines[1::2]))

        numbers_and_names = [' '.join((numbers[i], names[i])) for i in range(len(numbers))]
        self.problem_numbers_and_names = numbers_and_names

    def __replace_special_character(self) -> None:
        self.problem_numbers_and_names = list(map(
            StringEditor.replace_special_character,
            self.problem_numbers_and_names
        ))
    
    def __replace_space_to_underscore(self) -> None:
        self.problem_numbers_and_names = list(map(
            StringEditor.replace_space_to_underscore, 
            self.problem_numbers_and_names
        ))
    
    def __create(self) -> None:
        file_creator = FileCreator(self.created_directory, self.problem_numbers_and_names)
        file_creator.create_python_source()
        file_creator.create_input_text()

        file_editor = FileEditor(self.created_directory, self.problem_numbers_and_names)
        file_editor.insert_template_for_python()
        
    def __del__(self):
        self.problem_text.close()


class BOJProblemTemplateCreator(ProblemTemplateCreator):
    '''
    BOJ의 '단계별로 풀기' 페이지에 있는 문제들을 대상으로 함
    [주의]
    첫 번째 열인 '단계'도 포함해서 복사해야 함

    [입력 예시]  
    문제 링크: https://www.acmicpc.net/step/7
    3	10809	알파벳 찾기		74547	140624	53.041%
    한 단어에서 각 알파벳이 처음 등장하는 위치를 찾는 문제
    4	2675	문자열 반복	다국어	68687	135853	50.738%
    각 문자를 반복하여 출력하는 문제
    
    [결과 예시]
    10809_알파벳_찾기.py  
    2675_문자열_반복.py  
    '''

    def extract_numbers_and_names(self) -> None:
        problem_text_lines: list[str] = list(self.problem_text)
        for line in problem_text_lines:
            self.check_and_pick(line)

    def check_and_pick(self, line: str) -> None:
        word_group = line.split('\t')
        if word_group[0].isnumeric():
            number_and_name = ' '.join(word_group[1:3])
            self.problem_numbers_and_names.append(number_and_name)


if __name__ == "__main__":
    # ProblemTemplateCreator('problem_info.txt')()
    BOJProblemTemplateCreator('problem_info.txt', for_today=True)()