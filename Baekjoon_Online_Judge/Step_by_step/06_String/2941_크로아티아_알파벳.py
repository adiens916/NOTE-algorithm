import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline

# 0. 크로아티안 알파벳 첫 글자 세트와, 
# 해당 글자들로 시작하는 크로아티안 알파벳 후보들 준비
start_chars = set(('c', 'd', 'l', 'n', 's', 'z'))

# NOTE: 2차원 배열을 만들 때, 바깥쪽 튜플은 생략됨.
# 예: ([]) => [], (()) => ()
# 묶고 싶으면 리스트를 쓰자!
croatian = {
    'c': [['c=', 2], ['c-', 2]],
    'd': [['dz=', 3], ['d-', 2]],
    'l': [('lj', 2)],
    'n': [('nj', 2)],
    's': [('s=', 2)],
    'z': [('z=', 2)],
}

string = input().rstrip()
cur_idx = 0
count = 0

while cur_idx < len(string):
    # 1. 현재 글자가 크로아티안 알파벳일 가능성?
    if string[cur_idx] not in start_chars:
        # 첫 글자 세트에 없으면 그냥 일반 알파벳
        # 다음 글자 조사
        count += 1
        cur_idx += 1
        continue

    # 2. 크로아티안 알파벳일 가능성이 있으면,
    # 크로아티안 알파벳 후보들 하나씩 가져와서 비교
    for char, char_len in croatian[string[cur_idx]]:
        # 후보를 문자열에서 찾을 수 있는 경우
        # NOTE: 문자열 시작은 0보다 같거나 커야 함
        if string.find(char, cur_idx, cur_idx + char_len) >= 0:
            # NOTE: 알파벳 한 글자로 취급하므로 1씩 늘리기
            count += 1
            # 3. 매칭되면 해당 후보 길이만큼 현재 위치 옮기기
            cur_idx += char_len
            break
    # 후보에 해당하는 게 없었으면 1씩 증가
    else:
        count += 1
        cur_idx += 1

print(count)
