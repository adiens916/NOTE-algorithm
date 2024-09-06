"""
출처: https://www.acmicpc.net/source/76755103
참고: XXX로 주석 닮
"""


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
c_h = []
minimum = float("inf")

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            house.append([i, j])
        elif matrix[i][j] == 2:
            chicken.append([i, j])


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# XXX: 각 치킨집마다 모든 집까지의 거리를 미리 계산한 배열 만들기
for c in chicken:
    new_ch = []
    for h in house:
        new_ch.append(distance(c, h))
    c_h.append(new_ch)


def comb(arr, n):
    store = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        cur = arr[i]
        for c in comb(arr[i + 1:], n - 1):
            store.append([cur] + c)
    return store


def calc_min(arr):
    a = arr[0][:]
    for ar in arr[1:]:
        for i in range(len(a)):
            if a[i] > ar[i]:
                a[i] = ar[i]
    return sum(a)


# XXX: 치킨집 중 M개 봅으면, 각 치킨집마다 거리 배열 묶음이 나옴
for arr in comb(c_h, M):
    # XXX: 해당 거리 배열마다 거리 총합 구한 후, 최솟값과 비교
    temp = calc_min(arr)
    if minimum > temp:
        minimum = temp

print(minimum)