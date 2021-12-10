def powerset_using_bit():
    for subset in range(1 << N):
        case = []
        for k in range(N):
            if subset & 1 << k:
                case.append(arr[k])
        subsets.append(case)


arr = [3, 6, 9]     # 후보들
N = len(arr)

subsets = []

powerset_using_bit()
print(subsets)
