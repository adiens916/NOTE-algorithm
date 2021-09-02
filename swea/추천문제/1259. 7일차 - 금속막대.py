from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
임의의 정점을 기준으로 삼고,
한쪽 방향으로만 쭉 거슬러 올라가며
그 방향으로의 최장 길이를 구하는 함수.
(반대쪽도 같은 함수로 구함)
"""
def dfs_find_ends(arr, node, cur_len):
    global end_node
    global max_len

    # 최장 길이는 DFS로 구함.
    # 더 이상 못 가면 거기가 마지막.
    if not arr[node]:
        # 그 마지막일 때의 길이를 비교.
        if cur_len > max_len:
            max_len = cur_len
            end_node = node
        return cur_len
    else:
        # 만약 크기가 같은 나사가 여러 개인 경우?
        # 이 경우엔 각 나사에 대해 완전 탐색해봐야 함.
        kids = []
        for kid in arr[node]:
            length = dfs_find_ends(arr, kid, cur_len + 1)
            kids.append((kid, length))
        
        # 중간에 어떤 나사를 골라야 긴 쪽으로 갈지 모름.
        # -> 최대 길이로 가는 나사만 남겨놓자.
        kids.sort(key=lambda x: x[1])
        longer_one = kids[-1][0]
        arr[node] = [longer_one]

        # 길이를 돌려줘서 어느 자식/부모가 긴지 확인
        return kids[-1][1]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    edges = list(map(int, input().split()))

    # 앞쪽과 뒤쪽을 담을 배열 생성.
    parents_of = [[] for _ in range(101)]
    kids_of = [[] for _ in range(101)]
    for i in range(N):
        parent = edges[2 * i]
        kid = edges[2 * i + 1]
        parents_of[kid].append(parent)
        kids_of[parent].append(kid)
    
    end_node = 0
    # 맨 앞쪽 확인.
    max_len = 0
    dfs_find_ends(parents_of, edges[1], 0)
    first = end_node

    # 맨 뒤쪽 확인.
    max_len = 0
    dfs_find_ends(kids_of, edges[0], 0)
    last = end_node

    # 앞쪽 나사부터 뒤쪽 나사까지 짝지어 출력.
    print("#{}".format(test_case), end=" ")
    parent = first
    while kids_of[parent]:
        kid = kids_of[parent][0]
        print(parent, kid, end=" ")
        parent = kid
    print()
