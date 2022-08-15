import sys
sys.stdin = open("input.txt")


N = 8


def decreasing_queue(arr):
    front = 0
    rear = N - 1

    while True:
        for i in range(1, 6):
            rear = (rear + 1) % N
            arr[rear] = arr[front] - i
            front = (front + 1) % N

            # 0보다 작거나 같으면 0으로 바꿔주고 종료
            if arr[rear] <= 0:
                arr[rear] = 0

                # 큐를 구현하기 위해, 0이 맨 뒤로 가는 리스트 생성
                # 0 뒤에서부터 출발해 다시 0 있는 곳까지 오도록 함
                result = [arr[(rear + x) % N] for x in range(1, N + 1)]
                return result


T = 10
for test_case in range(1, T + 1):
    input()
    queue = [int(n) for n in input().split()]

    print("#{}".format(test_case), end=" ")
    print(*decreasing_queue(queue))
