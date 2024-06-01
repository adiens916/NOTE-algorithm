N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

# XXX: 원소를 서로 바꿔치기 할 필요없다.
# 어차피 B에서 최대인 K개를 뽑고, A에서 최대인 K개를 뽑는 것이기 때문.
max_sum = sum(B[0:K]) + sum(A[K:])
print(max_sum)

"""
5 3
1 2 5 4 3
5 5 6 6 5 
"""
