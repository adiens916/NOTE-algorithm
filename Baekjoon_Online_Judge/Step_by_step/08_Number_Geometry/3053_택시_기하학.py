import math
import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


R = int(input())

euclidean_circle_area = math.pi * R ** 2
print('%.6f' % euclidean_circle_area)

# D = x + y
# ∴ y = -x + D 의 그래프가 나온다!
# 택시 기하학에서의 원은 정사각형 마름모임.
taxis_circle_area = R ** 2 * 2
print('%.6f' % taxis_circle_area)

# 소수점 표현은 C와 같은 서식 지정자를 사용.
# 예) '%s' % '문자열'
# 참고: https://dojang.io/mod/page/view.php?id=2300