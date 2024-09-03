from sys import stdin
input = stdin.readline


# 통합된 연합을 찾고, 인구 이동을 수행하는 함수
def integrate(row, col, visited, date):
    global L, R, population, neigh

    # 초기 큐에는 현재 위치를 추가
    queue = [(row, col)]
    pivot = 0  # 큐의 시작 인덱스
    q_len = 1  # 큐의 길이 (탐색된 연합 크기)
    pop_tot = population[row][col]  # 현재 연합의 총 인구수
    visited[row][col] = date  # 현재 좌표를 방문 처리

    # BFS 방식으로 연합 탐색
    while pivot < q_len:
        r, c = queue[pivot]

        # 현재 위치의 이웃들을 순회
        for nr, nc in neigh[(r, c)]:
            # 날짜 정보로 방문 여부 확인, 인구 차이 조건 체크
            if (visited[nr][nc] < date) and (L <= abs(population[r][c] - population[nr][nc]) <= R):
                visited[nr][nc] = date  # 방문 처리
                queue.append((nr, nc))  # 연합에 추가
                pop_tot += population[nr][nc]  # 연합 인구수 갱신
                q_len += 1  # 연합 크기 증가

        pivot += 1  # 큐의 다음 인덱스로 이동

    return queue, q_len, pop_tot  # 연합 정보 반환


# 인구 이동 시뮬레이션을 수행하는 함수
def solve():
    global population

    # 초기 큐를 체스판의 흑백처럼 번갈아 가며 좌표를 설정하여 초기화
    queue = [(r, c) for c in range(N) for r in range(c % 2, N, 2)]
    visited = [[-1] * N for _ in range(N)]  # 방문 여부 초기화 (-1은 방문 안 함을 의미)

    for day in range(2000):
        next_q = []  # 다음 날 탐색할 좌표를 저장할 큐

        # 큐에 있는 모든 좌표를 순회하며 연합을 찾고, 인구 이동을 수행
        for r, c in queue:
            if visited[r][c] < day:  # 해당 좌표가 아직 방문되지 않았다면
                q, q_len, pop_tot = integrate(r, c, visited, day)  # 연합을 찾고 인구 이동

                if q_len > 1:  # 연합의 크기가 2 이상이라면 인구 이동이 발생한 것
                    avg = pop_tot // q_len  # 연합 내 평균 인구 계산
                    next_q += q  # 다음 탐색을 위해 연합의 모든 좌표를 큐에 추가
                    for x, y in q:
                        population[x][y] = avg  # 연합 내 모든 좌표에 대해 인구를 평균으로 갱신

        # 인구 이동이 더 이상 일어나지 않으면 종료
        if not next_q:
            print(day)  # 며칠 만에 인구 이동이 끝나는지 출력
            break
        else:
            queue = next_q  # 다음 날을 위해 큐를 갱신


# 메인 함수
if __name__ == "__main__":
    N, L, R = map(int, input().split())  # 격자의 크기(N)와 인구 이동 조건(L, R) 입력
    population = [list(map(int, input().split())) for _ in range(N)]  # 초기 인구 상태 입력
    neigh = {}  # 각 좌표의 이웃을 저장할 딕셔너리

    # 모든 좌표에 대해 이웃 좌표를 미리 계산하여 저장
    for r in range(N):
        for c in range(N):
            tmp = []
            for nr, nc in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
                if (0 <= nr < N) and (0 <= nc < N):  # 격자를 벗어나지 않는 이웃만 추가
                    tmp.append((nr, nc))
            neigh[(r, c)] = tmp  # 이웃 정보 저장

    solve()  # 시뮬레이션 실행