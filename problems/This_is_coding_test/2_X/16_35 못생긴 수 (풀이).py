N = int(input())

ugly = [0] * N
ugly[0] = 1

min_idx_for_2 = min_idx_for_3 = min_idx_for_5 = 0
mul_by_2, mul_by_3, mul_by_5 = 2, 3, 5

for i in range(1, N):
    ugly[i] = min(mul_by_2, mul_by_3, mul_by_5)

    # 이 if문은 모든 못생긴 수에 대해 2배씩 곱하는 것만 담당함.
    # 이를 위해, 이전에 설정한 값에 도달했는지 확인 후,
    if ugly[i] == mul_by_2:
        min_idx_for_2 += 1
        # 다음 못생긴 수를 찾고, 거기에 2배를 곱해서 설정함.
        mul_by_2 = ugly[min_idx_for_2] * 2
        # 그러다가 또 이 if 문에 걸리면, 다시 다음 못생긴 수에 대해 반복
        # 이런 식으로, 모든 못생긴 수에 대해 반복 작업 가능.

    if ugly[i] == mul_by_3:
        min_idx_for_3 += 1
        mul_by_3 = ugly[min_idx_for_3] * 3

    if ugly[i] == mul_by_5:
        min_idx_for_5 += 1
        mul_by_5 = ugly[min_idx_for_5] * 5

print(ugly[N-1])

