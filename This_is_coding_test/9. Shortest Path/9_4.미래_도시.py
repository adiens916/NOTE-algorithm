# Floyd-Warshall 알고리즘

from pathlib import Path
input_file = f"{Path(__file__).parent}\{Path(__file__).stem}_input.txt"

import sys
sys.stdin = open(input_file)
input = sys.stdin.readline


# 회사 개수, 경로 개수
N, M = map(int, input().split())

# 회사 연결 정보
INF = 2 ** 30
def init_graph(V: int):
    graph = [[INF] * (V + 1) for _ in range(V + 1)]

    for i in range(1, V + 1):
        graph[i][i] = 0
    
    return graph


graph = init_graph(N)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 목적지, 경유지
X, K = map(int, input().split())

# 플로이드-워셜 실행
# 경유지 k가 고정된 상태이므로, 중간에 더 짧은 경로로 갱신되는 일은 없음.
# 그러므로 a, b가 바뀌어도 값은 대각선을 기준으로 항상 대칭을 이룸.
# 예) 1번-3번-5번이나 5번-3번-1번이나 거리는 같음.
def floyd_warshall(graph: list[list[int]], V: int):
    for k in range(1, V + 1):
        for a in range(1, V + 1):
            for b in range(1, V + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


floyd_warshall(graph, N)
# (출발지~경유지~목적지) 값과 (목적지~경유지~출발지) 값이 같으므로,
# 어느 쪽을 기준으로 값을 구해도 (최솟값으로) 같다.
min_travel = graph[1][K] + graph[K][X]

if min_travel < INF:
    print(min_travel)
else:
    print(-1)
