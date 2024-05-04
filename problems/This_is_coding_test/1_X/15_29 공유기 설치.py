"""
XXX: 이진탐색에서 매 시행마다 N개씩 순회하면 NlogN

입력 범위 기준으로 보면, O(NlogN)이어야 한다는 건 알고 있었다.
다만 거기에 사로 잡혀서, 매번 N개를 전부 찾아 보는 건 생각도 못했다.

실제로 대략 계산해보면 매번 1/2씩 줄어드니까 logN이 소모되고,
그 매 시행마다 N개씩 전부 찾는다고 하면,
결국 NlogN이 소모된다.
"""


def main():
    n, c = map(int, input().split())
    points = [int(input()) for _ in range(n)]

    # 이진 탐색을 위한 정렬
    points.sort()

    # 이진 탐색을 통해 최적의 개수 구하기
    result = binary_search(n, c, points)
    print(result)


def binary_search(n: int, c: int, points: list[int]) -> int:
    optimal = 0

    # 최소 간격
    min_dist = 1
    # 최대 간격
    max_dist = points[n - 1] - points[0]
    while min_dist <= max_dist:
        # 임의로 최적 간격 계산
        dist = (min_dist + max_dist) // 2
        # 해당 최적 간격으로 몇 군데 설치할 수 있는지 계산
        count = count_points_over_optimal_distance(points, dist)

        # 설치 장소가 원하는 개수보다 적으면, 간격 줄여서 설치하기
        if count < c:
            max_dist = dist - 1
        # 원하는 개수보다 많으면, 간격 늘리기
        elif count > c:
            min_dist = dist + 1
        # 개수 같은 경우
        else:
            # XXX: 그냥 거리보다 먼 지점에 설치한 거고, 실제 지점 간의 거리와는 다를 수 있음.
            # 예: 1, 4는 거리가 2보다 멀어서 설치했지만, 실제로는 거리가 3 차이남.
            # => 개수 만족하는 한, 거리를 조금씩 더 늘리기
            min_dist = dist + 1
            optimal = dist

    return optimal


def count_points_over_optimal_distance(points: list[int], optimal: int) -> int:
    # 맨 처음 위치에 1개 설치
    prev = 0
    count = 1

    # 그 다음부터 마지막까지 순회 (O(N))
    for i in range(1, len(points)):
        #  현재 위치 - 이전 위치 거리가 최적 거리보다 큰 경우,
        if points[i] - points[prev] >= optimal:
            # 설치 가능
            count += 1
            prev = i

    return count


main()

"""
5 3
1
2
8
4
9
"""  # 3
