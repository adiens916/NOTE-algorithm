data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])

    # XXX: 현재까지의 결과가 1 이하인 경우에도 더하는 게 나음.
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
