"""
(10, 200)과 (200, 10)은 같은 덩치.
이 둘의 공통점은 몸무게와 키의 합이 같음!

: 몸무게가 크고, 키도 큰 경우,
몸무게와 키의 '합'도 크다.

! '크다'의 기준을 글자 말고 "수식"으로 제대로 써놓기

! 문제 예시에 현혹되지 말고, "조건" 보기
"만일 자신보다 더 큰 덩치의 사람이 k명이라면, 그 사람의 덩치 등수는 k+1"
= 누적 등수가 아니라, 오로지 자신을 기준으로만 비교 
"""

import sys
from pathlib import Path

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name}_input.txt")
input = sys.stdin.readline


def main():
    # 입력
    N = int(input())
    body_sizes = []
    for i in range(N):
        weight, height = map(int, input().split())
        body_sizes.append((weight, height, i))

    # 몸무게 + 키 합으로 정렬
    body_sizes.sort(key=lambda x: x[0] + x[1], reverse=True)

    # # 덩치 등수 배열 만들기
    body_ranks = [0] * N

    # 모든 사람을 기준으로 비교
    for i in range(N):
        cur_weight = body_sizes[i][0]
        cur_height = body_sizes[i][1]
        cur_index = body_sizes[i][2]

        # 자기보다 합이 큰 사람 중에, 덩치 큰 사람 찾기
        bigger_size_num = 0
        for j in range(i):
            prev_weight = body_sizes[j][0]
            prev_height = body_sizes[j][1]
            # 오직 자기 자신만 기준으로 해서 비교
            if cur_weight < prev_weight and cur_height < prev_height:
                bigger_size_num += 1

        body_ranks[cur_index] = bigger_size_num + 1

    print(*body_ranks)


main()
