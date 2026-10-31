import sys

def solve():
    # 입출력 성능 최적화로 데이터 전체 수집
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    # 회의 수 N 추출
    n = int(data[0])
    meetings = []
    
    # N개의 회의 정보를 튜플 (회의번호, 시작시간, 종료시간) 형태로 리스트에 저장
    idx = 1
    for _ in range(n):
        num = int(data[idx])
        start = int(data[idx+1])
        end = int(data[idx+2])
        meetings.append((num, start, end))
        idx += 3

    # 1순위 종료 시간(x[2]), 2순위 시작 시간(x[1]) 기준 오름차순
    meetings.sort(key=lambda x: (x[2], x[1]))

    selected = []       # 회의 번호를 담을 리스트
    last_end_time = 0   # 마지막으로 배정된 회의의 종료 시간

    # 그리디 선택 탐색
    for num, start, end in meetings:
        # 현재 회의 시작 시간이 이전 회의 종료 시간 이상이면 선택 가능
        if start >= last_end_time:
            selected.append(num)
            last_end_time = end  # 기준 종료 시간을 현재 회의 종료 시간으로 갱신

    # 결과 출력
    print(len(selected))  # 배정 가능한 최대 회의 수
    print(*selected)      # 배정한 회의 번호들을 공백 구분 출력

if __name__ == '__main__':
    solve()