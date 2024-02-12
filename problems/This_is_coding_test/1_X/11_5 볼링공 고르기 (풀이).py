N, M = map(int, input().split())
balls = list(map(int, input().split()))

counts_by_weight = [0] * (M + 1)
for weight in balls:
    counts_by_weight[weight] += 1

case_sum = 0
for i in range(1, M + 1):
    # XXX: 무게가 i인 볼링공의 개수 (A가 선택할 수 있는 개수) 제외
    N -= counts_by_weight[i]

    # XXX: B가 선택하는 경우의 수 곱하기
    # 바로 앞 단계에서 A가 선택할 수 있는 건 뺐으므로
    # 그냥 바로 곱하면 됨.
    case_sum += counts_by_weight[i] * N

print(case_sum)
