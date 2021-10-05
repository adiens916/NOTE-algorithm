from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def is_babygin(hands: list) -> bool:
    # 0부터 9까지
    for x in range(10):
        # 각 숫자부터 연속으로 3장이 있거나
        if hands[x] and hands[x + 1] and hands[x + 2]:
            return True
        # 혹은 해당 숫자가 3장 이상이거나
        if hands[x] >= 3:
            return True
    # 어느 것도 아니면 정답 없음
    return False


def play_babygin(deck):
    for i in range(6):
        # 홀수 번째 카드에 적힌 숫자를 1증가
        p1_hands[deck[2 * i]] += 1
        # babygin인지 확인
        if is_babygin(p1_hands):
            return 1
        
        p2_hands[deck[2 * i + 1]] += 1
        if is_babygin(p2_hands):
            return 2
    return 0


T = int(input())
for test_case in range(1, T + 1):
    p1_hands = [0] * 12
    p2_hands = [0] * 12

    deck = list(map(int, input().split()))
    result = play_babygin(deck)
    print('#{} {}'.format(test_case, result))
