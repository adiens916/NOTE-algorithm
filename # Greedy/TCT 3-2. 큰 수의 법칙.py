N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

max1 = max(arr)
arr.remove(max1)
max2 = max(arr)

# 반복되는 수열 파악하기
# => 가장 큰 수가 더해지는 횟수 계산
factor = M // (K + 1)
remain = M % (K + 1)

# 반복되는 수열 더하기
biggest_num = (max1 * K + max2) * factor
# 남은 횟수는 전부 큰 수에 몰빵
biggest_num += max1 * remain

print(biggest_num)
