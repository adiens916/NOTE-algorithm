def compress_by_unit(s: str, unit: int) -> str:
    result = ""
    anchor = 0

    while True:
        # 1. 기준이 되는 문자열이 끝까지 비교 가능한지 확인
        if anchor + unit > len(s):
            # 길이가 부족하면 그냥 끝까지 덧붙이기
            result += s[anchor:]
            return result

        moving = anchor
        equal_count = 1
        while True:
            moving += unit
            # 2. 비교하려는 문자열이 끝까지 비교 가능한지 확인
            if moving + unit > len(s):
                # XXX: 같은 게 1개는 무시
                if equal_count == 1:
                    # 기존 거 1개에 이후 거 쭉 이어서 반환
                    result += s[anchor:]
                else:
                    # 기존 거 여러 개 + 이후 거 따로 덧붙여서 반환
                    result += str(equal_count) + s[anchor : anchor + unit]
                    result += s[moving:]
                return result

            is_equal = True
            for i in range(unit):
                # 3. 서로 같은지 비교
                if s[anchor + i] != s[moving + i]:
                    is_equal = False
                    break

            # 같으면 다음으로 넘어가기
            if is_equal:
                equal_count += 1
            # 다르면 여태까지 확인한 걸 처리하기
            else:
                # XXX: 1개는 무시
                if equal_count == 1:
                    result += s[anchor : anchor + unit]
                else:
                    result += str(equal_count) + s[anchor : anchor + unit]
                # XXX: 일단 다르니까, 기준은 옮겨줘야 함.
                anchor += equal_count * unit
                break


def solution(s: str) -> int:
    min_str = s
    for unit in range(1, len(s) // 2 + 1):
        cur_str = compress_by_unit(s, unit)
        if len(min_str) > len(cur_str):
            min_str = cur_str

    answer = len(min_str)
    return answer


inputs = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
]
for ip in inputs:
    print(solution(ip))

"""
7
9
8
14
17
"""
