import sys

def get_1d_overlap(a1, a2, b1, b2):
    """
    1차원 구간 [a1, a2]와 [b1, b2]의 교차 상태를 반환합니다.
    """
    # 1. 아예 안 만나는 경우
    if a2 < b1 or b2 < a1:
        return "NULL"
    # 2. 한 점에서 접하는 경우
    elif a2 == b1 or b2 == a1:
        return "POINT"
    # 3. 선분 형태(면적)로 겹치는 경우
    else:
        return "FACE"

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # 박스 P, Q 좌표 입력받기
    px1, py1, px2, py2 = map(int, input_data[0:4])
    qx1, qy1, qx2, qy2 = map(int, input_data[4:8])

    # x축과 y축 각각 1차원 overlap 상태 구하기
    x_state = get_1d_overlap(px1, px2, qx1, qx2)
    y_state = get_1d_overlap(py1, py2, qy1, qy2)

    # 두 축의 상태를 조합하여 최종 교차 상태 결정
    if x_state == "NULL" or y_state == "NULL":
        print("NULL")
    elif x_state == "POINT" and y_state == "POINT":
        print("POINT")
    elif x_state == "FACE" and y_state == "FACE":
        print("FACE")
    else:
        # (POINT, FACE) 또는 (FACE, POINT) 조합인 경우
        print("LINE")

if __name__ == '__main__':
    solve()