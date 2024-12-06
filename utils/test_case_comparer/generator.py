from typing import List, Union

from element import Element, ElementList, Int, IntList


class TestCaseGenerator:
    @staticmethod
    def generate(template: List[List[Union[int, str]]]) -> str:
        if not template:
            raise ValueError("Template is empty or not provided.")
        # 템플릿에서 테스트 케이스를 생성
        test_case = TestCaseGenerator.load(template)
        return TestCaseGenerator.stringify(test_case)

    @staticmethod
    def load(template: List[List[Union[Element, ElementList, int]]]) -> List[List[int]]:
        """
        주어진 템플릿을 기반으로 테스트 케이스 생성

        :param template: Int 또는 int를 포함하는 여러 리스트들
        :return: 생성된 테스트 케이스들
        """
        result = []
        for line in template:
            line_after = []
            for val in line:
                if isinstance(val, Element):
                    line_after.append(val())
                elif isinstance(val, ElementList):
                    line_after.extend(val())
                elif isinstance(val, int):
                    line_after.append(val)
                else:
                    raise TypeError(f"Unsupported type: {type(val)} in template")
            result.append(line_after)
        return result

    @staticmethod
    def stringify(data: List[List[int]],
                  separator: str = ' ') -> str:
        """
        테스트 케이스를 문자열로 변환

        :param data: 변환할 테스트 케이스
        :param separator: 숫자 구분자
        :return: 문자열로 변환된 테스트 케이스
        """

        def stringify_line(lst):
            return separator.join(map(str, lst))

        return '\n'.join(stringify_line(line) for line in data)


# 사용 예시
if __name__ == "__main__":
    # 기본 사용법
    n = Int(0, 10)
    result = TestCaseGenerator.load([
        [1, 2, 3],
        [n, n, n],
        [10, IntList(0, 10, 1, 3), -1]
    ])
    print("생성된 테스트 케이스:")
    print(result)

    # 문자열 변환
    result_string = TestCaseGenerator.stringify(result)
    print("\n문자열 변환:")
    print(result_string)
