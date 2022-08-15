from collections import deque
import sys
sys.stdin = open("input.txt")


T = 10
for test_case in range(1, T + 1):
    input()
    queue = deque([int(n) for n in input().split()])
    dequeue = queue.popleft
    enqueue = queue.append

    i = 1
    while True:
        enqueue(dequeue() - i)

        if queue[-1] <= 0:
            queue[-1] = 0
            break

        i += 1
        if i == 6:
            i = 1

    print("#{}".format(test_case), end=" ")
    print(*queue)
