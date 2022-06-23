import time


def solution_1():
    def remove_center(arr: list[list[str]], row_start, col_start, N):
        length = N // 3

        for row in range(row_start + length, row_start + length * 2):
            for col in range(col_start + length, col_start + length * 2):
                arr[row][col] = ' '
        
        if length == 1:
            return

        for row in range(row_start, row_start + length * 2 + 1, length):
            for col in range(col_start, col_start + length * 2 + 1, length):
                remove_center(arr, row, col, length)


    N = 3 ** 5
    arr = [['*'] * N for _ in range(N)]
    remove_center(arr, 0, 0, N)

    for row in range(N):
        print(*arr[row], sep='')


def solution_2():
    def get_scaled_value(N, row, col):
        # 종료 조건은 N이 3일 때,
        if N == 3:
            # 가운데 부분의 좌표인 경우 빈 값
            if row == 1 and col == 1:
                return ' '
            # 가운데 이외는 *
            else:
                return '*'
        else:
            # 현재보다 더 작은 단위 계산
            scale = N // 3
            
            # 더 작은 단위에서 봤을 때 가운데 부분이면 빈 값
            if row // scale == 1 and col // scale == 1:
                return ' '
            # 가운데 부분이 아니면
            else:
                # 단위를 한 번 더 줄이면서 
                # 가운데인지 아닌지 계속 판단
                return get_scaled_value(
                    scale, 
                    row % scale, 
                    col % scale
                )


    N = 3 ** 5
    for row in range(N):
        for col in range(N):
            print(get_scaled_value(N, row, col), end='')
        print()


##################################################

def count_time(method):
    start = time.time()  # 시작 시간 저장
    method()
    end = time.time()
    return end - start  # 현재시각 - 시작시간 = 실행 시간


solutions = [solution_1]
times = []

for solution in solutions:
    cur_time = count_time(solution)
    times.append(cur_time)

for index, t in enumerate(times, start=1):
    print(f"function {index} time: {t} sec")
