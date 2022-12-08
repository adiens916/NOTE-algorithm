"""
2초 안에, 100000개까지, 각 이름은 20자까지
    - 딕셔너리
    - 이분탐색 <- 정렬 필요

알파벳 / 숫자
"""


import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline


N, M = map(int, input().split())
pokemon_names = {i: input().strip() for i in range(1, N + 1)}
pokemon_numbers = {v: k for k, v in pokemon_names.items()}

for i in range(M):
    question = input().strip()

    if question.isdigit():
        answer = pokemon_names[int(question)]
    else:
        answer = pokemon_numbers[question]

    print(answer)
