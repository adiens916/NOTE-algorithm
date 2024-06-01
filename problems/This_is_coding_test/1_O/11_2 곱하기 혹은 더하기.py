S = input()

nums = map(int, list(S))

total = 0
for num in nums:
    if num == 0:
        continue
    elif num == 1:
        total += 1
        continue

    # num > 1
    if total > 0:
        total *= num
    else:
        total = num


print(total)

"""
02984
567
00009
00101
11111
"""
# 576
# 210
# 9
# 2
# 5
