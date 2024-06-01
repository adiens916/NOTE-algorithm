N = int(input())

# 계수 정렬 이용
component_list = list(map(int, input().split()))
count_list = [0] * (1000000 + 1)
for component in component_list:
    count_list[component] += 1

M = int(input())

target_list = list(map(int, input().split()))

for target in target_list:
    if count_list[target] > 0:
        print("yes", end=" ")
        count_list[target] -= 1
    else:
        print("no", end=" ")

"""
5
8 3 7 9 2
3
5 7 9
"""
