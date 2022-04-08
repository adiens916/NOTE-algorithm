from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


# 조합 결과를 리스트로 반환
def nCr(n, r):
    result = []
    current = [None] * r
    def recur_nCr(start, chosen):
        # 개수만큼 뽑았으면 저장
        if r == chosen:
            result.append(tuple(current))
        else:
            # 조합: 앞으로 r번 반복문 중첩해 r개만큼 뽑아야 함
            # => 맨 처음 가능한 범위: 전부에서 r개만큼 제외
            # 이후, '앞에서 뽑은 만큼' 범위 늘려줘야 함
            for i in range(start, n - r + chosen + 1):
                current[chosen] = i
                recur_nCr(i + 1, chosen + 1)
    recur_nCr(0, 0)
    return result


def total_synergy(components: tuple):
    total = 0
    for i in range(len(components) - 1):
        for j in range(i + 1, len(components)):
            total += arr[components[i]][components[j]]
    return total


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_diff= 987654231

    # 1. 각 쌍의 시너지 합 미리 계산
    for row in range(N - 1):
        for col in range(row + 1, N):
            arr[row][col] += arr[col][row]
    
    # 2. 조합 구하기
    # 이때 A와 B는 가운데를 대칭으로 위치
    # => 한 칸씩 당겨오며 가져오면 됨.
    combinations = nCr(N, N // 2)
    for i in range(len(combinations) // 2):
        a = combinations[i]
        b = combinations[len(combinations) - 1 - i]
        # 3. 차이 구하기
        diff = abs(total_synergy(a) - total_synergy(b))
        if diff < min_diff:
            min_diff = diff
    
    print('#{} {}'.format(test_case, min_diff))
