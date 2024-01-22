N = int(input())
foods = list(map(int, input().split()))

max_foods = [0] * N
max_foods[0] = foods[0]
max_foods[1] = max(foods[0], foods[1])

for i in range(2, N):
    max_foods[i] = max(max_foods[i - 1], max_foods[i - 2] + foods[i])

print(max_foods[N - 1])


"""
4
1 3 1 5
"""
