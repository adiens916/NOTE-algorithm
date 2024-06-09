N = int(input())

tables = [0] * (N + 1)
tables[1] = 1
tables[2] = 3

for i in range(3, N + 1):
    # XXX: 나머지 값만 필요하므로, 결과 값 저장할 때도 나머지 이상은 필요 없음.
    tables[i] = (tables[i - 1] + tables[i - 2] * 2) % 796796

print(tables[N])
