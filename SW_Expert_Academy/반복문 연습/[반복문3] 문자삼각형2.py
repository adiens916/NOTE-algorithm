
from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def right_triangle(height, width_inc=1, start='A', top_line_num=1):
    # 오른 방향 삼각형은 행 & 열만 가지고 계산하기 복잡함
    # -> 그냥 평면 배열 만들고, 평면 이동하며 채워넣기
    # -> 주기로 나누는 것도 복잡하니, 그냥 문자만 가지고

    bottom_line_num = width_inc * 2 * (height - 1) + top_line_num

    arr = [[0] * height for _ in range(bottom_line_num)]
    row = bottom_line_num // 2  - top_line_num // 2
    col = height - 1

    line_num = 0
    line_num_max = top_line_num

    char = start
    
    while row < bottom_line_num:
        arr[row][col] = char
        
        # 문자를 다음 문자로 바꿔줌
        new_char = ord(char) + 1
        if new_char > ord('Z'):
            new_char = ord('A')
        char = chr(new_char)

        # 다음 행으로 넘어감
        row += 1
        line_num += 1

        # 마지막 행에 도달하면 종료
        if row == bottom_line_num:
            break
        
        # 각 층의 최대 길이를 넘어서면
        if line_num >= line_num_max:
            # 아래 층으로 넘어감
            col -= 1
            row = row - line_num_max - width_inc
            # 층의 길이 초기화
            line_num = 0
            line_num_max += width_inc * 2
    
    for row in range(bottom_line_num):
        for col in range(height):
            if arr[row][col]:
                print(arr[row][col], end=" ")
        print()



def right_triangle_width(width, width_inc=1, start='A', top_line_num=1):
    # FIXME: 문제에서 row 방향 길이를 물어봤으므로, 그에 맞게 다시 수정

    height = (width - top_line_num) // (width_inc * 2) + 1

    arr = [[0] * height for _ in range(width)]
    row = width // 2  - top_line_num // 2
    col = height - 1

    line_num = 0
    line_num_max = top_line_num

    char = start
    
    while row < width:
        arr[row][col] = char
        
        # 문자를 다음 문자로 바꿔줌
        new_char = ord(char) + 1
        if new_char > ord('Z'):
            new_char = ord('A')
        char = chr(new_char)

        # 다음 행으로 넘어감
        row += 1
        line_num += 1

        # 마지막 행에 도달하면 종료
        if row == width:
            break
        
        # 각 층의 최대 길이를 넘어서면
        if line_num >= line_num_max:
            # 아래 층으로 넘어감
            col -= 1
            row = row - line_num_max - width_inc
            # 층의 길이 초기화
            line_num = 0
            line_num_max += width_inc * 2
    
    for row in range(width):
        for col in range(height):
            if arr[row][col]:
                print(arr[row][col], end=" ")
        print()


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print("#{}".format(test_case))
    right_triangle_width(N)    
