"""
간격 값을 구한다.
해당 간격대로 공유기를 설치해본다.
공유기 개수를 센다.
공유기가 부족하면 거리를 줄인다.
공유기가 많으면 거리를 늘린다.
공유기가 같으면 거리를 늘린다.
"""
import sys
input = sys.stdin.readline


def count_available_setup_by_dist(arr, gap):
    setup = 1
    start = 0
    for i in range(1, len(arr)):
        if arr[start] + gap <= arr[i]:
            start = i
            setup += 1
    return setup


N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

min_d = 0
# XXX: 거리의 최댓값으로 비교
max_d = arr[N - 1]

answer = 0
while min_d <= max_d:
    mid = (min_d + max_d) // 2

    setup = count_available_setup_by_dist(arr, mid)
    if setup < C:
        max_d = mid - 1
    else:
        min_d = mid + 1
        answer = mid

print(answer)
