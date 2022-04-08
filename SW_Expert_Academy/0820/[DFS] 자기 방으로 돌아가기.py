from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline

"""
버스 노션 겹치는 문제랑 비슷
복도 구간이 겹치면 기다려야 하므로,
겹친 수만큼 단위 시간이 걸림
최대로 겹친 곳이 곧 정답
"""
"""
FIXME: 앗... 문제를 잘못 읽었다.
방이 일렬로 쭉 있는 게 아니라,
두 개의 열로 나뉘어져 있다...
이러면 2~3과 4~7이 3번&4번 복도에서 겹친다.

-> 테스트 케이스대로 그림을 그려보자!
"""
"""
FIXME: 엇... 출발지와 도착지가 순서대로 안 될 가능성도 있다.

-> 정렬된 상태로 들어온다는 말이 없으면, 무조건 정렬해서 비교!
"""

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    arr = []
    for i in range(N):
        s, e = map(int, input().split())
        # FIXME: 정렬 얘기 없었으니 정렬해서 비교
        # 예) 7번~3번 -> 3번~7번
        if e < s:
            s, e = e, s
        # FIXME: 3번과 4번은 같은 복도를 경유
        # -> 1 빼고 2로 나눠서 똑같은 지점으로 만들기
        # 예) 2번~3번 -> 0번~1번, 4번~7번 -> 1번~3번
        s, e = (s - 1) // 2, (e - 1) // 2
        arr.append((s, e))
    print(arr)

    max_cross = 0
    for p1 in range(N):
        cross = 0
        # FIXME: 각자 다른 점 -> 서로의 위치는 모름
        # -> 이전에 나온 구간들도 다시 체크
        for p2 in range(N):
            if arr[p2][0] <= arr[p1][0] and arr[p1][0] <= arr[p2][1]:
                cross += 1
        max_cross = cross if cross > max_cross else max_cross
    
    print("#{} {}".format(test_case, max_cross))

"""
출력
...
#4 3 
"""
