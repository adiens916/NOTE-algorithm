"""https://www.acmicpc.net/problem/2869"""

"""
1. 마지막 날에 시작할 때, 
    남은 거리가 A보다 작거나 같은 경우, 무조건 올라가고 끝남.
2. 이러려면 마지막 전날 밤에는, 최대 A만큼의 거리를 남겨야 함.
3. 마지막 전날 밤까지는 계속 (A-B)만큼 전진.
4. 결국 (A-B)로 V-A까지의 거리만큼 가는데 든 날짜 + 
    마지막 날에 A만큼 올라가고 끝나니까 1일이 필요함.

예) A = 5, B = 1, V = 14인 경우.
1. 마지막 날에 5만큼 남으면 올라가고 끝남.
2. 이를 위해선 전날에 9까지는 왔어야 함.
3. 4 * 2 + 1 = 9이므로, 2일만에는 못 오고 1일 더 필요.
4. 그럼 마지막 날에 13에서 출발하고, 1만큼 더 올라야 끝나므로 1일 필요.
이렇게 총 4일이 걸림.
"""

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


A, B, V = map(int, input().split())
distance = V - A
required_days = distance // (A - B)
if distance % (A - B):
    required_days += 1
print(required_days + 1)
