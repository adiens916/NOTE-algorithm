# 파스칼의 삼각형
memo = [[0] * (100+1) for _ in range(100+1)]
for i in range(100):
    for j in range(i+1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

def comb(n, r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return comb(n-1, r-1) + comb(n-1, r)

def comb2(n, r):
    if r == 0:
        print(T)
    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        comb2(n-1, r-1)
        comb2(n-1, r)

A = [1, 2, 3, 4]
N = len(A)
R = 3
T = [0] * R
# print(comb(50, 22))  #계산
print(memo[64][50])  #계산
# comb2(N, R)

