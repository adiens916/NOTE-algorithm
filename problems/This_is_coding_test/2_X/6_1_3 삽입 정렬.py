def insertion_sort(arr: list[int]) -> None:
    for start in range(1, len(arr)):
        for pre in range(start, 0, -1):
            # 한 지점과 그 이전만 살펴 보기
            if arr[pre] < arr[pre - 1]:
                arr[pre], arr[pre - 1] = arr[pre - 1], arr[pre]
            else:
                break

