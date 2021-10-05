from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]

    # 시작 시간 순으로 정렬 후, 그 안에서 또 종료 시간 순으로 정렬
    schedule.sort(key=lambda x: x[0])
    schedule.sort(key=lambda x: x[1])

    possible = 0
    max_possible = 0
    for i in range(N):
        # 남은 작업 개수가 현재까지의 최대 개수보다 같거나 작으면? 
        # 더 이상 진행해도 최대보다 커질 수 없음 => 중지
        if N - i <= max_possible:
            break

        # 매 스케쥴마다
        possible = 0
        for j in range(i + 1, N):
            # 앞의 종료 시간보다, 뒤의 시작 시간이 같거나 작으면 작업 가능
            if schedule[i][1] <= schedule[j][0]:
                possible += 1
                # 뒤쪽이 새로운 기준이 된다
                i = j
        
        # 맨 첫 번째는 무조건 작업 가능하므로, +1을 해줌
        max_possible = max(possible + 1, max_possible)

    print('#{} {}'.format(test_case, max_possible))
