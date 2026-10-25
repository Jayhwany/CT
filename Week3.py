import sys

def solve():
    # 전체 입력을 한 번에 받아서 정수 배열로 변환 (속도 최적화)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # 선분 데이터를 튜플 형태로 변환
    lines = []
    idx = 1
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input_data[idx:idx+4])
        lines.append((x1, y1, x2, y2))
        idx += 4

    intersect_count = 0

    # O(N^2) 교차 판정
    for i in range(n):
        x1, y1, x2, y2 = lines[i]
        for j in range(i + 1, n):
            x3, y3, x4, y4 = lines[j]

            # CCW 계산 인라인(Inline) 수행
            ccw123 = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
            ccw124 = (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)
            ccw341 = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
            ccw342 = (x4 - x3) * (y2 - y3) - (y4 - y3) * (x2 - x3)

            # 방향성 판별 (양수: 1, 음수: -1, 0: 0)
            c1 = 1 if ccw123 > 0 else (-1 if ccw123 < 0 else 0)
            c2 = 1 if ccw124 > 0 else (-1 if ccw124 < 0 else 0)
            c3 = 1 if ccw341 > 0 else (-1 if ccw341 < 0 else 0)
            c4 = 1 if ccw342 > 0 else (-1 if ccw342 < 0 else 0)

            r1 = c1 * c2
            r2 = c3 * c4

            if r1 == 0 and r2 == 0:
                # 일직선 상에 위치할 때 범위 비교
                p1, p2 = (x1, y1), (x2, y2)
                p3, p4 = (x3, y3), (x4, y4)
                if p1 > p2: p1, p2 = p2, p1
                if p3 > p4: p3, p4 = p4, p3
                if p3 <= p2 and p1 <= p4:
                    intersect_count += 1
            elif r1 <= 0 and r2 <= 0:
                intersect_count += 1

    print(intersect_count)

if __name__ == '__main__':
    solve()