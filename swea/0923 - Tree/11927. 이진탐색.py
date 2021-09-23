from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
이진 트리 생성: 올라가며 대소 비교, 내려오며 대소 비교

1. 삽입된 쪽 서브 트리 바닥 -> 루트까지 거슬러 올라옴
2. 루트를 지나서 맞은 편으로 이동
3. 맞은 편 꼭대기부터 -> 바닥까지 이동

i) 형제 없음 & 부모보다 큼 -> 부모랑만 치환
ii) 형제 있음 & 부모보다 큼 -> '회전'
    

"""

def make_binary_tree(N):
    tree = []
    for i in range(1, N + 1):
        tree.append(i)
