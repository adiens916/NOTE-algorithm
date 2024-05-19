def find_parent(x: int, parents: list[int]) -> int:
    if parents[x] != x:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


G = int(input())
P = int(input())
flights = [int(input()) for _ in range(P)]


count = 0
parents = [i for i in range(G + 1)]
for flight in flights:
    available = find_parent(flight, parents)
    if available == 0:
        print(count)
        break
    else:
        # 루트까지 가는 곳 전부 갱신하기
        # 2에서 1 줄이고
        # 3의 루트를 1로 함
        # (2의 루트도 1로 함)
        count += 1


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