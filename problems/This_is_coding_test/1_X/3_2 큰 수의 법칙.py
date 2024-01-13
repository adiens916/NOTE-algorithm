N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
largest1 = nums[0]
largest2 = nums[1]

rep_count = int(M / (K + 1))
rep_num = largest1 * K + largest2

remaining_count = M % (K + 1)

answer = rep_num * rep_count + largest1 * remaining_count
print(answer)
