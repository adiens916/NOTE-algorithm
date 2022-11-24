import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


def main():
    N = int(input())
    deque = Deque(N)

    for _ in range(N):
        inputs = input().split()
        func = deque.__getattribute__(inputs[0])
        arg = inputs[1] if len(inputs) == 2 else None

        result = func(arg)
        # ! result가 None이 아닌지 명시해서 판단하기
        # result가 0일 때 출력 안 될 수 있음.
        print(result) if result is not None else None


class Deque:
    def __init__(self, N: int) -> None:
        self.deque = [0] * N
        self.max_size = N
        self.count = 0
        self.head = -1
        self.tail = -1

    def push_front(self, elem: int) -> None:
        # 앞으로 이동
        self.head -= 1

        # 이동 후 인덱스 유효한지 체크
        if self.head < 0:
            self.head = self.max_size - 1

        # 넣기
        self.deque[self.head] = elem
        self.count += 1

        # 1개만 있을 때는 처음-끝 모두 같음
        if self.count == 1:
            self.tail = self.head

    def push_back(self, elem: int) -> None:
        self.tail += 1

        if self.tail > self.max_size - 1:
            self.tail = 0

        self.deque[self.tail] = elem
        self.count += 1

        if self.count == 1:
            self.head = self.tail

    def pop_front(self, _=None) -> int:
        # 비어있으면 pop 불가
        if self.empty():
            return -1

        # 빼기
        elem = self.deque[self.head]
        self.count -= 1

        # 뒤로 이동
        self.head += 1

        # 이동 후 인덱스 유효한지 체크
        if self.head > self.max_size - 1:
            self.head = 0

        # 1개인 경우 처음-끝 모두 같아야 함
        if self.count == 1:
            self.tail = self.head

        return elem

    def pop_back(self, _=None) -> int:
        if self.empty():
            return -1

        elem = self.deque[self.tail]
        self.count -= 1

        self.tail -= 1

        if self.tail < 0:
            self.tail = self.max_size - 1

        if self.count == 1:
            self.head = self.tail

        return elem

    def size(self, _=None) -> int:
        return self.count

    def empty(self, _=None) -> int:
        return 1 if self.count == 0 else 0

    def front(self, _=None) -> int:
        if self.empty():
            return -1

        return self.deque[self.head]

    def back(self, _=None) -> int:
        if self.empty():
            return -1

        return self.deque[self.tail]


main()
