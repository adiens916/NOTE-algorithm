"""
정렬 하지 않고 푸는 방법.
어차피 가운데 있는 숫자를 찾는 거니까,
전체에서 절반에 오는 숫자를 찾으면 됨.
이를 위해 계수 정렬 이용함.

출처: https://www.acmicpc.net/source/52750687
"""

k = int(input())
houses = list(map(int, input().split()))

# 계수 정렬
counts = [0 for i in range (100001)]
for house in houses:
    counts[house] += 1

cnt = 0
for house in range(100001):
    cnt += counts[house]
    # 절반 넘어가는 곳이면
    if cnt >= (k + 1) // 2:
        # 거기가 중앙에 있는 지점임.
        print(house)
        break
