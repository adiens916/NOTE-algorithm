"""
가장 긴 증가하는 수열을 이진탐색으로 풀기
아이디어 출처: https://cocoon1787.tistory.com/713
코드 출처: https://sunho-doing.tistory.com/entry/BOJ-12015-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-2
"""

from bisect import bisect_left
import sys
input = sys.stdin.readline


n = int(input())
powers = list(map(int, input().split()))

# 가장 긴 증가하는 수열을 저장할 배열
dp = [powers[0]]

for i in range(1, n):
    # 현재 원소가, 가장 긴 증가하는 수열의 마지막보다 큰 경우
    if powers[i] > dp[-1]:
        # 수열 길이를 늘려줌
        # 왜냐하면 수열이 유지되는 경우이므로.
        dp.append(powers[i])

    # 현재 원소가, 가장 긴 증가하는 수열의 마지막보다 작은 경우
    else:
        # 기존 수열 중에 늘릴 수 있는 위치 찾기
        idx = bisect_left(dp, powers[i])
        # 해당 위치의 원소와 교환
        # 이러는 이유는, 어차피 길이만 보는 것이기 때문
        dp[idx] = powers[i]

print(len(dp))
