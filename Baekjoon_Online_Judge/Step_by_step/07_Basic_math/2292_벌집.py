"""https://www.acmicpc.net/problem/2292"""

"""
숫자 범위가 매우 크므로, 수식으로 풀어야 함.
시작 ~ 끝 범위와, 해당 범위 안에 있을 때의 값을 적기.

    1   = 1칸
2  ~ 7  = 2칸
8  ~ 19 = 3칸
20 ~ 37 = 4칸
38 ~ 61 = 5칸

규칙성을 찾기

        6*0+1 = 1
6*0+2 ~ 6*1+1 = 2
6*1+2 ~ 6*3+1 = 3
6*3+2 ~ 6*6+1 = 4
6*6+2 ~ 6*10+1 = 5

끝 범위에서 6을 제외하고 보면 1, 3, 6, 10으로
계차수열의 형태를 보이고 있음.
"""


import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline



start = 0
end = 1
increment = 1

N = int(input())
if N == 1:
    print(1)
else:
    while True:
        if 6 * start + 2 <= N <= 6 * end + 1:
            print(increment + 1)
            break
        else:
            start = end
            increment += 1
            end += increment
