from pathlib import Path
import sys


parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    pairs = list(map(int, input().split()))
    parent_of = [0] * (E + 2)   # 부모 노드
    child_num = [0] * (E + 2)   # 서브 트리의 노드 개수 

    for i in range(E):
        parent, child = pairs[2 * i], pairs[2 * i + 1]
        # 부모 노드 저장
        parent_of[child] = parent

        # 루트 노드까지 거슬러 올라가며
        # 서브 트리 개수가 1 증가한 걸 갱신
        while parent:
            child_num[parent] += 1
            parent = parent_of[parent]
    
    print('#{} {}'.format(test_case, child_num[N] + 1))
