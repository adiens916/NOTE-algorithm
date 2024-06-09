# 출처: https://velog.io/@suzieep/Algorithm-이코테-1로-만들기-파이썬
# 바텀 업으로 푸는 게 훨씬 효율적
# 왜냐하면 -1 연산 때문에, 결국 모든 수를 다 찾아봐야 하기 때문임.

X = int(input())

table = [0] * (X + 1)

# 1은 이미 됐으니까, 2부터 시작
for i in range(2, X + 1):
    table[i] = table[i - 1] + 1
    # 기존 테이블 값 비교 후 계속 갱신
    if i % 2 == 0:
        table[i] = min(table[i], table[i // 2] + 1)
    if i % 3 == 0:
        table[i] = min(table[i], table[i // 3] + 1)
    if i % 5 == 0:
        table[i] = min(table[i], table[i // 5] + 1)

print(table[X])
