def main():
    N, K = list(map(int, input().split()))
    print(binomial_coefficient(N, K))


def binomial_coefficient(N: int, K: int):
    if K > N // 2:
        K = N - K

    numerator = 1
    for i in range(N - K + 1, N + 1):
        numerator *= i

    denominator = 1
    for i in range(1, K + 1):
        denominator *= i

    return numerator // denominator


main()
