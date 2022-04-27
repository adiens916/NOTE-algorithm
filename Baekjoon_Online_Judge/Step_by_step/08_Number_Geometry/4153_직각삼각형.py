import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    
    x = min(min(a, b), c)
    z = max(max(a, b), c)
    y = (a + b + c) - (x + z)

    if x ** 2 + y ** 2 == z ** 2:
        print('right')
    else:
        print('wrong')
