from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


# by 효전님
# 딕셔너리를 이용해 트리를 생성
def build_tree(V, E, edges):
    tree = {i: {"parent": 0, "children": []} for i in range(V + 1)}
    for i in range(E):
        parent = edges[2 * i]
        child = edges[2 * i + 1]
        tree[parent]["children"].append(child)
        tree[child]["parent"] = parent
    return tree


# by 재성님
# 부모 리스트를 만들어서 교집합을 찾는 방식
def find_common_ancestor(child1, child2):
    # 자손들의 부모들을 집어넣을 리스트
    parent_list = [0] * (V + 1)

    # 첫 번째 자식의 부모들을 체크
    parent = tree[child1]["parent"]
    # 루트까지 체크 (루트의 부모는 0임)
    while parent:
        # 부모 리스트에 해당 부모를 표시
        parent_list[parent] += 1
        parent = tree[parent]["parent"]
    
    # 두 번째 자식의 부모들을 체크
    parent = tree[child2]["parent"]
    while parent:
        # 첫 번째 자식의 부모와 같다면
        if parent_list[parent] == 1:
            return parent
        parent = tree[parent]["parent"]


# by 영준님
# 스택을 이용해 순회
def traverse(node):
    count = 0
    stack = [tree[node]["children"]]

    while stack:
        children = stack.pop()
        for child in children:
            stack.append(tree[child]["children"])
        count += 1

    return count


T = int(input())
for test_case in range(1, T + 1):
    V, E, child1, child2 = map(int, input().split())
    edges = list(map(int, input().split()))

    tree = build_tree(V, E, edges)
    ancestor = find_common_ancestor(child1, child2)
    traverse_count = traverse(ancestor)

    print("#{} {} {}".format(test_case, ancestor, traverse_count))
