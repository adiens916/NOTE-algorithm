"""
17_38 정확한 순위 풀 때랑 비슷함.

다만 거기서는 서로 상대적인 순위만 나와서,
우선 플로이드-워셜로 전부 이어주는 작업이 필요했음.

반면 여기서는 이미 전체 순위가 나와 있으므로,
뒤바뀐 순위만 처리하면 됨.
"""

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        prev_ranks = list(map(int, input().split()))
        M = int(input())
        reversed_pairs = [list(map(int, input().split())) for _ in range(M)]
        check_ranks(N, prev_ranks, reversed_pairs)


def check_ranks(N, prev_ranks, reversed_pairs) -> None:
    # 이차원 배열을 만들기
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        cur_num = prev_ranks[i]
        for j in range(i):
            # 행에서 열로 갈 수 있으면 (즉, 자신보다 등수가 높으면)
            high_num = prev_ranks[j]
            # 배열[행][열]에 1 집어넣기
            arr[cur_num][high_num] = 1

    # 등수가 바뀌면
    for pair in reversed_pairs:
        a, b = pair
        # 해당 [행][열] 값을 서로 교환하기
        arr[a][b], arr[b][a] = arr[b][a], arr[a][b]

    cur_ranks = [0] * N
    for i in range(1, N + 1):
        # 행에 1이 들어있는 개수 = 자신의 전체 등수가 됨.
        higher_count = sum(arr[i])
        team_num = cur_ranks[higher_count]

        # 이 전체 등수가 겹치면 실패고,
        if team_num != 0:
            print("IMPOSSIBLE")
            return
        # 겹치지 않는 경우 그대로 출력하면 전체 등수가 나옴.
        else:
            cur_ranks[higher_count] = i

    print(*cur_ranks, sep=' ')


main()

"""
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
"""
"""  # 
5 3 2 4 1
2 3 1
IMPOSSIBLE
"""
