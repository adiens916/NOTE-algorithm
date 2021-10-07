from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 번갈아 가며 찾은 횟수
    alternatingly_found = 0

    # B에 속한 정수들 각각에 대해 A에 들어있는지 조사
    for target in B:
        # 시작 & 끝 초기화
        left = 0
        right = N - 1
        # 마지막 영역을 나타내는 변수
        last_bound = ''

        while left <= right:
            mid = (left + right) // 2
            # 더 큰 쪽인데, 저번에도 큰 쪽이면 나감
            if A[mid] < target:
                if last_bound == '<':
                    break
                # 아니면 마지막 영역 기록 후, 다음 영역 검색
                last_bound = '<'
                left = mid + 1
            # 더 작은 쪽
            elif A[mid] > target:
                if last_bound == '>':
                    break
                last_bound = '>'
                right = mid - 1
            # 같은 경우
            else:  
                # 찾은 횟수 1 증가
                alternatingly_found += 1 
                break
    
    print('#{} {}'.format(test_case, alternatingly_found))
