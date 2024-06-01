N = input()

numbers = list(map(int, list(N)))

right_start = len(numbers) // 2
right_sum = sum(numbers[right_start:])
left_sum = sum(numbers[:right_start])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")


"""
123402
"""  # LUCKY
"""
7755
"""  # READY
