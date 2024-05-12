"""
Idea: https://velog.io/@thguss/%EC%BD%94%ED%85%8C-%EC%8A%A4%ED%84%B0%EB%94%94-DP-%EB%AA%BB%EC%83%9D%EA%B8%B4-%EC%88%98
Code & Tip: https://techblog-history-younghunjo1.tistory.com/303
"""

n = int(input())
ugly = [0] * n
# 첫 번째 못 생긴 수는 1
ugly[0] = 1

num_by_2, num_by_3, num_by_5 = 0, 0, 0
cnt2, cnt3, cnt5 = 0, 0, 0

for i in range(1, n):
    # 최솟값 판단
    ugly[i] = min(num_by_2, num_by_3, num_by_5)

    # 2의 배수인 경우
    if ugly[i] == num_by_2:
        # 곱할 2의 개수 1개 더 늘리기
        cnt2 += 1
        # cnt2번째에 해당하는 수에 2 곱하기
        num_by_2 = ugly[cnt2] * 2

    # elif가 아니라 if인 이유는, 같은 최소공배수 값에 2배, 3배, 5배를 해줘야 하기 때문임.
    # elif로 하면 최소공배수 값들이 따로 계산되어 여러 개 중복으로 들어감.
    if ugly[i] == num_by_3:
        cnt3 += 1
        num_by_3 = ugly[cnt3] * 3
    if ugly[i] == num_by_5:
        cnt5 += 1
        num_by_5 = ugly[cnt5] * 5

print(ugly[n - 1])
