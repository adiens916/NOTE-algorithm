"""
두 배열 원소를 최대 K번 바꿔치기해서,
한 배열의 모든 원소의 합이 최대가 되게
"""

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

for i in range(K):
    # FIXME: '최대' => 클 때만 바꿔야 함
    if A[i] < B[i]:
        A[i] = B[i]
    else:
        break

print(sum(A))

"""
5 3
1 2 5 4 3
5 5 6 6 5
"""
