"""
N+1일 때 퇴사 = N+1 이상이면 불가
상담일에 시작일 포함

하는 경우 vs. 안 하는 경우
1일(~3일) + 4일째까지의 금액 vs. 2일째까지의 금액
"""

N = int(input())
days = [list(map(int, input().split())) for _ in range(N)]

table = [0] * (N + 1)
# 맨 뒤에 있는 날짜부터 거슬러 올라오며 계산
for today in range(N - 1, -1, -1):
    time, pay = days[today]

    if today + time > N:
        # 기간이 퇴사일을 넘기면 상담 불가
        # XXX: continue를 하면 안 됨. 다음 날 기록을 그대로 가져 와야 함.
        table[today] = table[today + 1]
    else:
        # 오늘의 수익 비교
        # 이때 마지막 날이 가능한 경우도 있으니, table 크기를 1 늘려줬음.
        table[today] = max(pay + table[today + time], table[today + 1])

print(table[0])

"""
반례 출처: https://www.acmicpc.net/board/view/138171
3
5 10
2 10
1 10
"""  # 10
