from pathlib import Path
import sys

parent_dir = Path(__file__).parent
file_name = Path(__file__).stem

sys.stdin = open(f"{parent_dir}\{file_name} input.txt")
input = sys.stdin.readline


T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case}", end=" ")

    max_drop = 0

    block_num = int(input())
    blocks = list(map(int, input().split()))

    # 중력 영향 때문에 바닥에서부터(=뒤에서부터) 올라가며 확인
    for base in range(block_num - 1, -1, -1):
        drop = 0

        # 기본적으로 정렬 방식:
        # 블럭을 만나면 
        if blocks[base] > 0:
            # 밑에서부터 올라오며 어디에 쌓일지 확인
            for down in range(block_num - 1, base, -1):
                # 자신보다 작은 블럭이 나오면 그 자리에 들어가야 한다.
                # 왜냐하면 여분의 블럭이 그 자리까지 떨어지기 때문
                if blocks[down] < blocks[base]:
                    # 다른 블럭들은 위로 한 칸씩 밀어준다.
                    # 블럭들이 밑에 있는 개수만큼 겹치는데,
                    # 결국 위로 한 칸씩 밀리는 형태가 됨.
                    original_block = blocks[base]
                    for k in range(base, down):
                        blocks[k] = blocks[k + 1]
                    blocks[down] = original_block

                    # 낙차 계산
                    drop = down - base
                    break
            else:
                # 자신보다 작은 게 없다면 떨어지지 않는다.
                pass
            
            # 낙차 최대치를 갱신한다.
            max_drop = drop if drop > max_drop else max_drop

    print(max_drop) 


# 출력
#1 7
#2 7
#3 16