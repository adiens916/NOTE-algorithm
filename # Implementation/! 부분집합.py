def add_subset(case):
    """
    포함하기로 결정된 원소들만 뽑아
    부분집합으로 추가
    """
    subset = []
    for i in range(N):
        if case[i]:
            subset.append(arr[i])
    subsets.append(subset)


def powerset(k):
    """
    부분집합에 포함할 원소를 결정
    """
    if k == N:  # 후보 전부 순회 시 경우 추가
        add_subset(case)
    else:
        case[k] = True  # 포함하기로 함
        powerset(k + 1) # 다른 후보들에 대해서도 시행

        case[k] = False # 안 포함
        powerset(k + 1) # 다른 후보들에 대해서도 시행


arr = [3, 6, 9]     # 후보들
N = len(arr)        # 후보 개수

case = [False] * N  # 각 부분집합
subsets = []        # 전체 부분집합

powerset(0)
print(subsets)
