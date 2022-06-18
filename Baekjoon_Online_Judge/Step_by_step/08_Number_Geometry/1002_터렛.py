'''
두 좌표 사이의 거리를 L이라고 할 때,
만나는 경우
1) 좌표도 같고, 거리도 같은 경우: L = 0, r1 = r2
2) 접점이 한 개인데, 다른 원 안에 포함: r1 + L = r2
3) 접점이 하나인 경우: L = r1 + r2
4) 접점이 두 개인 경우: L < r1 + r2

안 만나는 경우
5) 중심은 같은데, 거리는 다름
6) 다른 원 포함하는데 접하진 않음
7) 아예 서로 떨어져 있음

'''

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    # 제곱근을 씌우면 실수가 되어 오차 발생
    # => 제곱으로 비교하기
    L = (x1 - x2) ** 2 + (y1 - y2) ** 2

    # 좌표가 겹칠 때
    if L == 0:
        # 반지름 같으면 원 겹침
        if r1 == r2:
            print(-1)
        # 반지름 다르면 서로 안 만남
        else:
            print(0)
    # 좌표가 다를 때
    else:
        # 한 원이 다른 원 안에 있을 때
        if L == (r1 - r2) ** 2:
            print(1)
        elif L < (r1 - r2) ** 2:
            print(0)
        # 한 원이 다른 원 안에 없을 때
        elif L == (r1 + r2) ** 2:
            print(1)
        elif L < (r1 + r2) ** 2:
            # 원이 서로 겹치는 경우.
            # 원래 L > r2 - r1 조건이 필요하나
            # 앞의 분기들을 거치면서 조건 충족하게 됨.
            print(2)
        elif L > (r1 + r2) ** 2:
            print(0)