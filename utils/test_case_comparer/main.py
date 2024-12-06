import sys
import io
from typing import Callable, List, Union

from generator import Int, TestCaseGenerator


class InputHandler:
    """입력을 처리하는 헬퍼 클래스"""

    @staticmethod
    def replace_stdin(input_data: str):
        sys.stdin = io.StringIO(input_data)


class TestCaseComparer:
    def __init__(self):
        """
        메서드 비교를 위한 초기화
        """
        self.methods = []
        self.template = None

    def set_template(self, template: List[List[Union[Int, int]]]):
        """
        테스트 케이스 템플릿 설정

        :param template: 테스트 케이스 템플릿 리스트
        """
        self.template = template

    def add(self, method: Callable):
        """
        비교할 메서드 추가

        :param method: 비교할 함수
        """
        self.methods.append({
            'func': method,
            'name': method.__name__
        })

    def compare(self, n: int = 1):
        """
        메서드들의 결과 비교

        :param n: 실행 반복 횟수
        """
        for test_index in range(1, n + 1):
            # 테스트 케이스 생성
            test_case = self._generate_test_case()

            # 메서드 결과 비교
            method_results = self._collect_method_results(test_case)
            self._compare_results(method_results, test_index, test_case)

    def _generate_test_case(self) -> str:
        """
        템플릿을 기반으로 테스트 케이스 생성

        :return: 생성된 테스트 케이스 문자열 리스트
        """
        if self.template is None:
            raise ValueError("Template not set. Use set_template() first.")
        return TestCaseGenerator.generate(self.template)

    def _collect_method_results(self, test_case):
        """
        각 메서드의 결과를 수집합니다.

        :param test_case: 테스트 케이스
        :return: 메서드 결과 리스트
        """
        method_results = []

        for method_info in self.methods:
            method = method_info['func']
            method_name = method_info['name']

            # 입력 대체
            InputHandler.replace_stdin(test_case)

            try:
                result = method()
                method_results.append({
                    'name': method_name,
                    'result': result
                })
            except Exception as e:
                print(f"Error in method '{method_name}': {e}")

        return method_results

    def _compare_results(self, method_results, test_index, test_case):
        """
        메서드 결과를 비교합니다.

        :param method_results: 메서드 결과 리스트
        """
        if len(method_results) > 1:
            baseline = method_results[0]['result']

            for result in method_results[1:]:
                if result['result'] != baseline:
                    print(f"Test Case {test_index}:")
                    print(f"Input: {test_case}")
                    print(f"Result1: {baseline}")
                    print(f"Method '{result['name']}' DIFFERENT:")
                    print(f"Result2: {result['result']}")
                    print()  # 테스트 케이스 간 구분


# 사용 예시
if __name__ == "__main__":
    def method1():
        a, b = map(int, input().split())
        return a + b


    def method2():
        a, b = map(int, input().split())
        return int(a) + int(b) + 1


    # 비교기 설정
    cmp = TestCaseComparer()

    # 템플릿 설정
    n = Int(0, 100)
    cmp.set_template([
        [n, n],  # 랜덤 숫자 2개
        # [1, 2]  # 고정 숫자
    ])

    # 메서드 추가
    cmp.add(method1)
    cmp.add(method2)

    # 비교 실행 (3번 반복)
    cmp.compare(n=3)
