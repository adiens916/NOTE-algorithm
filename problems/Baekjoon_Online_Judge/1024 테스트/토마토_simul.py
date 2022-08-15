from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name.rsplit('_')[0]} input.txt")
input = sys.stdin.readline


"""
1. 상태 검사: 전부 순회하면서 체크
2. 상태 변경
    - 델타 배열
    - 방문 배열
    - 순회
        - 트리거?
        - 아직 안 방문?
            방문하기

            주변부 순회
            범위 체크 & 방문 체크
            하려는 작업 실시
"""


def is_all_tomatoes_ripe():
    for height in range(H):
        for width in range(W):
            for breadth in range(B):
                if boxes[height][width][breadth] == 0:
                    return False
    return True


B, W, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(W)] for _ in range(H)]
day = 0

if is_all_tomatoes_ripe():
    print(day)
    exit()

# 앞 뒤 왼쪽 오른쪽 위 아래
dh = (0, 0, 0, 0, 1, -1)
dw = (0, 0, -1, 1, 0, 0)
db = (-1, 1, 0, 0, 0, 0)
# 앞쪽, 왼쪽, 아래쪽은 이미 지나온 곳들
# => 1로 채워도 문제없음
will_not_visit = (True, False, True, False, False, True)

visited = [[[False] * B for _ in range(W)] for _ in range(H)]

# 상태가 바뀌는 게 없을 때까지 계속해서 반복
changed = False
while True:
    for height in range(H):
        for width in range(W):
            for breadth in range(B):
                # 트리거(익은 토마토)인 경우
                if boxes[height][width][breadth] == 1:
                    # 방문 체크 후, 바로 방문하기
                    if not visited[height][width][breadth]:
                        visited[height][width][breadth] = True
                        
                        # 주변부 탐색
                        for i in range(6):
                            h = height + dh[i]
                            w = width + dw[i]
                            b = breadth + db[i]

                            # 범위 체크 & 방문 체크
                            if not (0 <= h < H and 0 <= w < W and 0 <= b < B): continue
                            if visited[h][w][b]: continue

                            # 타겟(안 익은 토마토)인 경우,
                            if boxes[h][w][b] == 0:
                                # 이미 지나온 곳은 그대로 1로 채우기
                                if will_not_visit[i]:
                                    boxes[h][w][b] = 1
                                # 앞으로 지날 곳을 1로 채우면? 
                                # 그 줄은 하루만에 끝까지 1로 채워져서 안 됨
                                # => 임의로 다른 값을 채워놓음
                                else:
                                    boxes[h][w][b] = 2
                                changed = True
                # 당일 타겟이 된 토마토
                # 당일 순회에 휘말리지 않도록 바꿔놓고 스킵
                elif boxes[height][width][breadth] == 2:
                    boxes[height][width][breadth] = 1

    # 한 번이라도 상태가 바뀐 적이 있으면 계속 반복
    if changed:
        day += 1
        changed = False
    else:
        break

if is_all_tomatoes_ripe:
    print(day)
else:
    print(-1)
