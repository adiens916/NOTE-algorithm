"""
전략
1. 0이 있거나 범위 벗어나면 방향 바꾸기
2. 열에서 행으로 바뀔 때 거리가 1씩 감소
"""

def snail_numbers(N):
    # 움직이는 유형
    move_x = (1, 0, -1, 0)
    move_y = (0, 1, 0, -1)
    # 어느 유형인지
    mode = 0

    arr = [[0] * N for _ in range(N)]
    reach = N
    num = 1
    row = 0
    col = -1

    while num <= N * N:
        for _ in range(reach):
            row += move_y[mode]
            col += move_x[mode]
            arr[row][col] = num
            num += 1
        
        # 방향 바꾸기
        mode = (mode + 1) % 4
        # 열 방향에서 행 방향으로 바뀔 때만 거리 감소
        if mode % 2 == 1:
            reach -= 1
        
    for n in range(N):
        print(*arr[n])


T = int(input())
for test_case in range(1, T + 1):
    print("#{}".format(test_case))
    N = int(input())
    snail_numbers(N)