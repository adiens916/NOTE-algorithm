from pathlib import Path
parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

import sys
sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


# 후보자 수만큼의 점수 배열
score_sum = [0] * 3
# 후보자 수만큼의 점수 개수의 배열 (1번 후보자의 1점, 2점, 3점 ~ 3번 후보자)
score_counts = [[0] * 4 for _ in range(3)]

N = int(input())
for _ in range(N):
    scores = map(int, input().split())
    # 점수는 후보자 순으로 들어오므로,
    # 해당 후보자의 해당 점수 개수를 1증가
    for candidate, score in enumerate(scores):
        score_counts[candidate][score] += 1
        score_sum[candidate] += score

# 후보자 대신, 점수 개수를 기준으로 다시 묶음 (1점 개수의 1번, 2번, 3번 후보자)
candidate_scores = list(zip(*score_counts))

index = -1
# 최고가 한 개 있으면 해당 인덱스가 우승
if score_sum.count(max(score_sum)) == 1:
    index = score_sum.index(max(score_sum))
else:
    # 3점부터 2점까지 비교
    # FIXME: 1점까지 비교하면 1점 점수가 제일 높은 애(=다른 건 점수 낮은 애)가 우승...
    for i in range(3, 1, -1):
        if candidate_scores[i].count(max(candidate_scores[i])) == 1:
            index = candidate_scores[i].index(max(candidate_scores[i]))
            break
    # 전부 비긴 경우 -1
    else:
        index = -1

print(index + 1, max(score_sum))
