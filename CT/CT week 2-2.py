import sys

def solve():
    # 빠른 입력 처리 및 데이터 읽기
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    board = []
    
    idx = 1
    for _ in range(n):
        row = [int(x) for x in data[idx:idx+n]]
        board.append(row)
        idx += n

    white_count = 0  # 하얀색(0) 색종이 수
    blue_count = 0   # 파란색(1) 색종이 수

    # 분할 재귀 함수 정의
    def divide(r, c, size):
        nonlocal white_count, blue_count
        
        color = board[r][c]  # 현재 영역의 기준 색상 
        is_same = True

        # 현재 영역이 전부 같은 색인지 검사
        for i in range(r, r + size):
            for j in range(c, c + size):
                if board[i][j] != color:
                    is_same = False
                    break
            if not is_same:
                break

        # 모두 같은 색이면 색종이 수 카운트 후 종료
        if is_same:
            if color == 0:
                white_count += 1
            else:
                blue_count += 1
            return

        # 색이 섞여 있으면 4개의 영역으로 잘라 재귀 호출
        half = size // 2
        divide(r, c, half)                # 1사분면 (좌상)
        divide(r, c + half, half)         # 2사분면 (우상)
        divide(r + half, c, half)         # 3사분면 (좌하)
        divide(r + half, c + half, half)  # 4사분면 (우하)

    # (0, 0) 위치에서 한 변의 길이가 N인 전체 종이 탐색 시작
    divide(0, 0, n)

    # 최종 결과 출력
    print(white_count)
    print(blue_count)

if __name__ == '__main__':
    solve()