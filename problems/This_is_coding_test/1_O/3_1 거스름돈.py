coins = [500, 100, 50, 10]
count = 0

remains = int(input())
for coin in coins:
    count += remains // coin
    remains %= coin

print(count)
