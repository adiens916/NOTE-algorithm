from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
왔던 경로 되돌아가기 가능 & 최소 '종류'
=> 양 점을 잇는 선 하나만 오가면 최소임
=> 최소 간선 개수 = 정점 개수 - 1
"""

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    _ = [input() for _ in range(E)]

    # adj_list = [[] for _ in range(V + 1)]
    # for _ in range(E):
    #     s, e = map(int, input().split())
    #     adj_list[s].append(e)
    #     adj_list[e].append(s)
    
    print(V - 1)
