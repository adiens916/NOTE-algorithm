from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
# input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[int(n) for n in input()] for _ in range(N)]

    profit = 0
    for y in range(N):
        # 가운데를 중심으로 위아래 모양이 대칭
        # -> 가운데를 넘어서면 작은 쪽 행으로 바꾸기
        line = y
        if line > N//2:
            line = N//2 * 2 - y
        
        # 행이 늘수록 가운데를 중심으로 넓어짐
        # -> 가운데에서 행 번호를 빼고 더하는 식으로 늘림
        left = N//2 - line
        right = N//2 + line
        for x in range(left, right + 1):
            profit += arr[y][x]
    
    print("#{} {}".format(test_case, profit))
