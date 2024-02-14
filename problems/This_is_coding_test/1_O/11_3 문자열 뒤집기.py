S = input()

alter_count = 0
prev = S[0]

# 0 혹은 1이 바뀌는(교차하는) 횟수 세기
for num in S:
    if prev != num:
        alter_count += 1
        prev = num

# 교차하는 개수를 1, 2, 3, ... 쭉 쓰다 보면 다음과 같은 규칙성이 나옴.
# 결국 가운데 끼여있는 쪽을 바꾸는 게 횟수가 더 작기 때문.
inverted_count = (alter_count + 1) // 2
print(inverted_count)

"""
0001100
11111
00000001
11001100110011000001
11101101
"""  # 1, 0, 1, 4, 2
