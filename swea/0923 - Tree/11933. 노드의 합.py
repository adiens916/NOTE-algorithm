from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
리프 노드에만 값이 있음 
-> 리프 노드들부터 거슬러 올라가며 값을 더하면 됨
-> 부모 노드의 값은 자연스레 채워짐
"""

T = int(input())
for test_case in range(1, T + 1):
    node_num, leaf_num, target_node = map(int, input().split())
    
    tree = [0] * (node_num + 1)
    for _ in range(leaf_num):
        node, value = map(int, input().split())
        tree[node] = value
    
    # 딱 리프 노드의 개수만큼만 부모들에 더해줌
    # 만약 모든 노드에 대해 처리하면 부모들 값이 또 더해짐
    for node in range(node_num, node_num - leaf_num, -1):
        value = tree[node]
        while node // 2:
            tree[node // 2] += value
            node //= 2
    
    target_value = tree[target_node]
    print('#{} {}'.format(test_case, target_value))
