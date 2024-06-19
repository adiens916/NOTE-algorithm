"""
1. 1부터 X까지 만들 수 있다고 하자.
2. 만약 새로운 동전 Y가 추가된다고 하면,
추가로 1+Y부터 X+Y까지 만들 수 있음.
3. 1과 2의 범위를 합치면 [1, X] + [1+Y, X+Y]

4. 위 두 범위가 합쳐지기 위해선,
1+Y가 X+1이랑 같거나, 더 작아야 함.
즉, 1+Y <= X+1
Y <= X

5. 반대로 Y > X인 경우엔 위 범위가 이어지지 않고 떨어짐.
6. 즉, 새로 추가된 동전 Y가 X보다 크면,
이어지지 않으므로, X+1이 답임.
"""

N = int(input())
coins = list(map(int, input().split()))
coins.sort()

max_ = 1
for coin in coins:
    if max_ < coin:
        break
    else:
        max_ += coin

print(max_)

"""
5
3 2 1 1 9
"""  # 8
"""
3
3 5 7
"""  # 1
