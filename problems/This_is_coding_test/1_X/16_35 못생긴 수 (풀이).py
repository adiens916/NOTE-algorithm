"""
Idea: https://velog.io/@thguss/%EC%BD%94%ED%85%8C-%EC%8A%A4%ED%84%B0%EB%94%94-DP-%EB%AA%BB%EC%83%9D%EA%B8%B4-%EC%88%98
Code & Tip: https://techblog-history-younghunjo1.tistory.com/303
"""

n = int(input())
ugly = [0] * n
# 첫 번째 못 생긴 수는 1
ugly[0] = 1

num_by_2, num_by_3, num_by_5 = 2, 3, 5
index_for_2, index_for_3, index_for_5 = 0, 0, 0

for i in range(1, n):
    # 최솟값 판단은 여기서 이뤄짐.
    ugly[i] = min(num_by_2, num_by_3, num_by_5)

    # 아래부터는 다음 못생긴 수를 만드는 과정.
    # 2의 배수인 경우
    if ugly[i] == num_by_2:
        # 이전 위치에서 한 칸 뒤로 가기
        # 이런 식으로 **인덱스를 분리**함으로써, 모든 숫자에 대해 2를 곱하게 됨.
        index_for_2 += 1
        # 해당 못생긴 수에 2를 곱해서 새로운 못생긴 수를 후보에 올리기
        num_by_2 = ugly[index_for_2] * 2

    # elif가 아니라 **if인 이유는, 같은 숫자(최소공배수)에** 2배, 3배, 5배를 각각 해줘야 하기 때문임.
    # 그래야 모든 경우에 대한 못생긴 수를 얻을 수 있음.
    # elif로 하면 최소공배수 값들이 따로 계산되어 여러 개 중복으로 들어감.
    if ugly[i] == num_by_3:
        index_for_3 += 1
        num_by_3 = ugly[index_for_3] * 3

    if ugly[i] == num_by_5:
        index_for_5 += 1
        num_by_5 = ugly[index_for_5] * 5

    # 같은 숫자에 대해 모든 if를 거치므로, 적어도 하나는 값이 변했을 거임.
    # 그렇다면 최솟값도 변했을 거고, 결국 매번 최솟값이 커짐.
    # 즉, 모든 경우를 적용함으로써, 이전에 나왔던 최솟값이 또 나오는 일은 없게끔 보장함.

print(ugly[n - 1])

"""
10
"""  # 12
"""
4
"""  # 4
