from collections import Counter
import sys
from pathlib import Path

input_txt = Path(__file__).with_suffix(".txt")
sys.stdin = open(input_txt)
input = sys.stdin.readline

MAX = 10000000


def main():
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    cards_to_pick = list(map(int, input().split()))

    # count_cards(cards, cards_to_pick)
    count_cards_by_counter(cards, cards_to_pick)


def count_cards(cards: list[int], cards_to_pick: list[int]):
    positive_num_cards = [0] * (MAX + 1)
    negative_num_cards = [0] * (MAX + 1)

    for card in cards:
        if card >= 0:
            positive_num_cards[card] += 1
        else:
            negative_num_cards[-card] += 1

    for card in cards_to_pick:
        if card >= 0:
            print(positive_num_cards[card], end=" ")
        else:
            print(negative_num_cards[-card], end=" ")


def count_cards_by_counter(cards: list[int], cards_to_pick: list[int]):
    counter = Counter(cards)
    card_counts = [counter.get(card, 0) for card in cards_to_pick]
    print(*card_counts, sep=" ")


main()
