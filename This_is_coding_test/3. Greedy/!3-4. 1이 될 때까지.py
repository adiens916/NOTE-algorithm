N, K = map(int, input().split())
count = 0

# while N > 1:
#     if N % K:
#         N -= 1
#     else:
#         N //= K
#     count += 1

while N > 1:
    # 나머지가 있는 경우
    if N % K:
        # 1씩 빼는 대신 한꺼번에 빼기
        # 나머지가 곧 뺀 횟수
        count += N % K
    # 몫으로 나누기
    N //= K
    count += 1

print(count)
