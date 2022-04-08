from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


from collections import deque


T = int(input())
for test_case in range(1, T + 1):
    oven_num, pizza_num = [int(n) for n in input().split()]
    # 피자 인덱스와 값으로 리스트 구성
    pizzas = [(i, int(n)) for i, n in enumerate(input().split())]
    last = 0

    # 피자 리스트에서 화덕 개수만큼 가져와 큐 생성
    oven = deque(pizzas[:oven_num])
    # 피자 개수는 줄어듦
    pizza_num -= oven_num

    # 오븐에 피자가 하나라도 있는 동안
    while oven:
        # 1번 자리 피자를 꺼냈을 때 치즈가 0이 아니라면
        # 치즈를 반 줄이고 다시 넣기
        if oven[0][1] // 2:
            i, n = oven.popleft()
            oven.append((i, n // 2))
        # 치즈가 0이면
        else:
            # 피자의 인덱스만 따로 저장
            last, _ = oven.popleft()
            # 아직 남아있는 피자가 있다면
            if pizza_num:
                # 해당 피자를 끝에서부터 세서 집어넣고, 피자 개수 감소
                oven.append(pizzas[-pizza_num])
                pizza_num -= 1
    
    print("#{} {}".format(test_case, last + 1))
