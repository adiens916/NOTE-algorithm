from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    
    buy = [False] * N
    for x in range(N):
        for y in range(x + 1, N):
            if buy[x] == False and prices[x] < prices[y]:
                buy[x] = True
                break
    
    cost = 0
    count = 0
    margin = 0
    for x in range(N):
        if buy[x]:
            cost += prices[x]
            count += 1
        else:
            margin += count * prices[x]
            margin -= cost
            cost = 0
            count = 0
    
    print("#{} {}".format(test_case, margin))

    # max_price = prices[N - 1]
    # margin = 0
    # for x in range(N - 2, -1, -1):
    #     if prices[x] < max_price:
    #         margin += max_price - prices[x]
    #     else:
    #         max_price = prices[x]
    # print("#{} {}".format(test_case, margin))
