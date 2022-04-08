from itertools import permutations


print(permutations(range(5), 3))


def nPr(n, r, k):
    """
    n개 중 r개를 뽑는 순열
    - n: 원소의 전체 개수
    - r: 뽑아야 하는 개수
    - k: 현재까지 뽑은 원소의 개수
    """
    if k == r:
        print(case)
    else:
        for i in range(n):      # 모든 원소 순회
            if not used[i]:     # 사용된 적이 없으면 
                used[i] = True  # 사용됨으로 표시
                case[k] = arr[i]  # 순열에 사용
                nPr(n, r, k + 1)
                used[i] = False # 다른 자리에서 사용 가능

N = 5
R = 3
arr = list(range(N))    # 순열에 쓰일 후보 목록
used = [False] * N      # 사용 여부
case = [0] * R          # 순열을 저장하는 배열
nPr(N, 3, 0)


def nTTr(n, r, k):
    """
    중복순열 = 순열 - 방문 체크 부분 제거 => 재방문 가능
    - n: 원소의 전체 개수
    - k: 현재 레벨
    """
    if k == r:
        print(case)
    else:
        for i in range(n):          # 모든 원소 순회
                case[k] = arr[i]    # 순열에 사용
                nTTr(n, r, k + 1)

N = 3
arr = list(range(N))
case = [0] * N
nTTr(N, N, 0)