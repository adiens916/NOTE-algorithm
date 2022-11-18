"""
< 사용 방법 >
1. solution_1, solution_2 함수마다 
비교하고 싶은 코드 통째로 넣으면 됩니다.

    입력 값이 필요한 경우,
    직접 적어주든 / 인자로 넘기든
    편한 방법으로 하면 됩니다.

2. 실행하면 걸린 시간을 콘솔에 출력합니다.


< 응용 >
여러 함수를 비교하고 싶은 경우,
solution_3, solution_4 등을 추가하고
main() 함수의 solutions에 추가하면 됩니다.

"""
import time


def main():
    solutions = [solution_1, solution_2]
    run(solutions)


def solution_1():
    """예시 1: 큐를 이용하여 앞뒤만 조작해서 빠름"""
    from collections import deque

    def main():
        # N = int(input())
        N = 200000
        print(pick_from_queue(N))

    def pick_from_queue(N: int):
        nums = [i for i in range(1, N + 1)]
        queue = deque(nums)
        pick = -1

        while queue:
            pick = queue.popleft()
            if queue:
                queue.append(queue.popleft())

        return pick

    main()


def solution_2():
    """예시 2: 리스트 중간 요소를 인덱스로 제거해서 느림"""

    def main():
        # N = int(input())
        N = 200000
        print(pick_from_queue_by_index(N, 2))

    def pick_from_queue_by_index(N: int, gap: int):
        """느림"""
        nums = [i for i in range(1, N + 1)]
        index = 0
        pick = -1

        while nums:
            pick = nums.pop(index)

            if len(nums) > 0:
                index = (index + gap - 1) % len(nums)

        return pick

    main()


##################################################
# 아래 내용은 바꿀 필요 없음


def run(solutions):
    times = []

    for solution in solutions:
        cur_time = count_time(solution)
        times.append(cur_time)

    print()
    for index, t in enumerate(times, start=1):
        print(f"function {index} time: {t} sec")


def count_time(method):
    start = time.time()  # 시작 시간 저장
    method()
    end = time.time()
    return end - start  # 현재시각 - 시작시간 = 실행 시간


main()
