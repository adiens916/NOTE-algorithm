import time


def main():
    solutions = [solution_1]
    run(solutions)


def solution_1():
    pass


def solution_2():
    pass


##################################################


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
