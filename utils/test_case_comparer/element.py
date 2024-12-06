from abc import ABC, abstractmethod
import random


class Element(ABC):
    @abstractmethod
    def __call__(self):
        pass


class Int(Element):
    def __init__(self, min_val: int, max_val: int):
        """
        범위를 가진 정수 생성기

        :param min_val: 최소값
        :param max_val: 최대값
        """
        self.min_val = min_val
        self.max_val = max_val

    def __call__(self) -> int:
        """
        인스턴스를 직접 호출하면 랜덤 정수 반환
        """
        return random.randint(self.min_val, self.max_val)


class ElementList(ABC):
    @abstractmethod
    def __call__(self):
        pass


class IntList(ElementList):
    def __init__(self, min_val: int, max_val: int, min_len: int, max_len: int):
        self.min_val = min_val
        self.max_val = max_val
        self.min_len = min_len
        self.max_len = max_len

    def __call__(self) -> list[int]:
        length = random.randint(self.min_len, self.max_len)
        return [random.randint(self.min_val, self.max_val) for _ in range(length)]
