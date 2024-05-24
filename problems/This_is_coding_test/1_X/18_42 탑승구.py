def find_parent(x: int, parents: list[int]) -> int:
    if parents[x] != x:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


G = int(input())
P = int(input())
flights = [int(input()) for _ in range(P)]

# 탑승구 정보를 루트 노드로 가짐
parents = [i for i in range(G + 1)]

count = 0
for flight in flights:
    # 해당 탑승구 정보 가져옴
    parent = find_parent(flight, parents)
    # 만약 탑승구가 0을 가리키면 (즉, 남는 탑승구가 없으면) 종료
    if parent == 0:
        break
    else:
        # 가능한 탑승구 숫자를 줄여야 함
        # 일단 루트 노드의 숫자도 한 개 줄이고
        parents[parent] = parent - 1
        # 루트 노드가 옮겨 갔으니, 현재 탑승구의 루트 노드도 갱신
        parents[flight] = parent - 1
        count += 1

print(count)

"""
4
3
4
1
1
"""  # 2
"""
4
6
2
2
3
3
4
4
"""  # 3
"""
3
3
3
=> 3, 2, 1

3
3
1
=> 3, 2, 1

3
1
3
=> 3, 1, 2

3
2
2
=> 3, 2, 1

2
2
3
=> 2, 1, 3

: 3에 도착하면
3의 루트 찾기

루트가 0이면
이미 3개는 다 썼음.

루트가 0이 아니면
3에서 1 줄이고
2를 루트로 함.


또 3에 도착하면
이번엔 루트가 2에 있음.

2에서 1 줄이고
3의 루트를 1로 함
(2의 루트도 1로 함)
"""