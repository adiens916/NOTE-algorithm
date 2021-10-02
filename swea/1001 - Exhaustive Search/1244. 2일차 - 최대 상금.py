from pathlib import Path
import sys


parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


def swap(max_swap, swap_times):
    # 교환 횟수만큼 교환했으면 종료
    if max_swap == swap_times: 
        return
    else:
        for i in range(0, length - 1):
            for j in range(i + 1, length):
                # 서로 교환
                numbers[i], numbers[j] = numbers[j], numbers[i]

                # 재귀 실행
                # + 가지치기 (이미 했던 거는 제외)
                swap_result = ''.join(numbers)
                if swap_result not in swap_results[swap_times]:
                    swap_results[swap_times].append(swap_result)
                    swap(max_swap, swap_times + 1)
                
                # 원위치
                numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())
for test_case in range(1, T + 1):
    numbers, max_swap = input().split()
    length = len(numbers)
    numbers = list(numbers)
    max_swap = int(max_swap)

    swap_results = [[] for _ in range(max_swap)]
    swap(max_swap, 0)

    print(f'#{test_case} {max(swap_results[max_swap - 1])}')
