from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def complete_binary_min_heap(arr):
    N = len(arr)
    heap = [0] * (N + 1)

    for i in range(1, N + 1):
        # 1. 끝에 노드 추가
        heap[i] = arr[i - 1]
        # 2. 부모와 대소 비교
        while i // 2:
            if heap[i] < heap[i // 2]:
                # 3. 부모와 치환
                heap[i], heap[i // 2] = heap[i // 2], heap[i]
                i //= 2
            else:
                break
    
    return heap


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = complete_binary_min_heap(arr)

    node_sum = 0
    i = N
    while i // 2:
        node_sum += heap[i // 2]
        i //= 2
    
    print('#{} {}'.format(test_case, node_sum))
