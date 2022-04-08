from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def permutation(cols, depth, N, cur_sum):
    global arr
    global min_sum

    if depth < N:
        for c in range(depth, N):
            # 가지치기 부분
            # 기준이 될 수 있는 곳들마다 값을 구해서 기존 합에 더함
            # 그 값이 최소 합보다 커지면 넘김
            new_base_val = arr[depth][cols[c]]
            if cur_sum + new_base_val > min_sum:
                continue

            # 기준을 바꿔줬으므로, 이 값을 기존 합에 더해서 넘김
            cols[depth], cols[c] = cols[c], cols[depth]
            permutation(cols, depth + 1, N, cur_sum + new_base_val)
            cols[depth], cols[c] = cols[c], cols[depth]
    else:
        # 위에서 최소 합보다 크면 넘어가게 했으므로
        # 끝까지 도착한 건 최소 합보다 작거나 같음
        min_sum = cur_sum


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cols = list(range(N))
    # 10 미만의 정수 * N 행이므로, 최댓값은 10 * N
    min_sum = 10 * N

    permutation(cols, 0, len(cols), 0)

    print("#{} {}".format(test_case, min_sum))
