"""
오늘까지 = max(오늘 + n만큼 떨어진 날까지, 어제까지)
"""


n = int(input())
counsels = [list(map(int, input().split())) for _ in range(n)]

max_rewards = [0] * n
for day in range(n - 1, -1, -1):
    time, reward = counsels[day]

    reward = reward if day + time <= n else 0
    tomorrow_reward = max_rewards[day + 1] if day + 1 < n else 0
    nth_day_reward = max_rewards[day + time] if day + time < n else 0

    max_rewards[day] = max(reward + nth_day_reward, tomorrow_reward)

print(max_rewards[0])

"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""  # 45
"""
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
"""  # 90
