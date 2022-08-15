import sys
sys.stdin = open('이진힙_input.txt')
def heap_push(value):
    global heap_count
    heap_count += 1   # 마지막노드번호 증가
    heap[heap_count] = value  # 마지막 노드에 값 저장
    current = heap_count   # 마지막 노드가 현재 노드
    parent = current // 2   # 부모노드
    # 루트가 아니고, 부모 노드의 값이 더 크면 -> swap
    while parent and heap[parent] > heap[current]:
        heap[parent], heap[current] = heap[current], heap[parent]
        current = parent
        parent = current // 2

def find_node():
    parent = heap_count // 2
    sum = 0
    while parent:
        sum += heap[parent]
        parent = parent // 2

    return sum

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0] * (N+1)    # 이진힙
    temp = list(map(int, input().split()))

    heap_count = 0 #힙의 갯수
    for i in range(N):
        heap_push(temp[i])

    ans = find_node()
    print(f'#{tc} {ans}')