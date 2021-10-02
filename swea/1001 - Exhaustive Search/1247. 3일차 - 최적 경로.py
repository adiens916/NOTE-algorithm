from pathlib import Path
import sys


parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


"""
최단 경로 방문 문제 => 순열 (완전탐색)

순열 => 항상 처음부터 끝까지 도는 대신 방문 배열로 구분

+ 하나씩 선택하는 과정에서 매번 최단 거리와 비교하여 가지치기 가능
(가지치기는 방문 직전에)
"""


def permutation(visit_times, cur_path):
    global min_path
    # 다 방문했을 때
    if customer_num == visit_times:
        # 회사와 집 경로도 거리에 포함시키기
        first_x, first_y = customers[visit_list[0]]
        last_x, last_y = customers[visit_list[-1]]
        cur_path += abs(work_x - first_x) + abs(work_y - first_y) \
            + abs(last_x - home_x) + abs(last_y - home_y)   
        
        # 최솟값 갱신
        min_path = min(cur_path, min_path)
        # print(visit_list, cur_path)
        return
    else:
        # 순열 -> 처음부터 돌면서 체크
        for i in range(customer_num):
            # 체크했던 건 방문 배열로 확인
            if not visited[i]:
                # 가지치기 작업: 마지막 고객과 현재 고객 사이의 거리 구하고
                # 이 값을 더했는데 최솟값보다 크다? => 더 작은 값 안 나옴
                this_path = 0
                if visit_times > 0:
                    last_x, last_y = customers[visit_list[visit_times - 1]]
                    this_x, this_y = customers[i]
                    this_path = abs(last_x - this_x) + abs(last_y - this_y)
                    # FIXME: cur_path += this_path로 했더니 값이 더 크게 나옴
                    # <- 이번뿐 아니라 다음번 고객 체크할 때도 반영되기 때문
                    # => 값은 따로 나누자!
                    if cur_path + this_path > min_path:
                        continue
                
                visited[i] = True
                visit_list[visit_times] = i
                permutation(visit_times + 1, cur_path + this_path)
                visited[i] = False
                    

T = int(input())
for test_case in range(1, T + 1):
    customer_num = int(input())
    work_x, work_y, home_x, home_y, *coords = list(map(int, input().split()))
    customers = [[coords[2*i], coords[2*i + 1]] for i in range(customer_num)]

    visited = [False] * customer_num  # 방문 체크 배열
    visit_list = [0] * customer_num  # 현재 방문 경로 리스트
    min_path = 200 * 12

    permutation(0, 0)  # 방문 횟수 0, 현재 경로도 0
    print(f'#{test_case} {min_path}')
