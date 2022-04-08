# 한 번 게산된 결과를 메모이제이션 하기 위한 리스트 초기화
mem = [0] * 100

# 피보나치 함수 구현
def fibonacci(N):
    # 종료 조건
    if N == 1 or N == 2:
        return 1
    
    # 아직 계산된 적이 없으면
    if not mem[N]:
        # 계산해서 값을 저장
        mem[N] = fibonacci(N - 1) + fibonacci(N - 2)
    # 저장된 값 반환
    return mem[N]

print(fibonacci(99))
