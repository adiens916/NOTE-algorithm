"""
기둥은 바닥 위 / 보의 한쪽 끝 부분 위 / 다른 기둥 위
보는 한쪽 끝 부분이 기둥 위 / 양쪽 끝 부분이 다른 보와 연결

삭제 후에도 규칙 만족해야 함. 만족 안 될시 해당 작업 무시.

벽면을 벗어나거나 바닥에 보를 설치하는 경우는 없음. => 범위 검사 X
구조물이 겹치거나, 없는 구조물을 삭제하는 경우는 없음. => 일단 설치하거나 삭제는 가능.

교차점 좌표 기준, 보는 오른쪽, 기둥은 위쪽
"""


def solution(n, build_frame):
    answer = set()

    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:  # 삭제
            answer.discard((x, y, a))
            if not is_available(answer):
                answer.add((x, y, a))
        else:  # 설치
            answer.add((x, y, a))
            if not is_available(answer):
                answer.discard((x, y, a))

    answer = sorted(answer)
    return answer


def is_available(answer: set) -> bool:
    for x, y, frame in answer:
        if frame == 0:  # 기둥
            if y == 0:
                continue
            elif (x - 1, y, 1) in answer or (x, y, 1) in answer:
                continue
            elif (x, y - 1, 0) in answer:
                continue
            else:
                return False

        else:  # 보
            if (x, y - 1, 0) in answer or (x + 1, y - 1, 0) in answer:
                continue
            elif (x - 1, y, 1) in answer and (x + 1, y, 1) in answer:
                continue
            else:
                return False

    return True
