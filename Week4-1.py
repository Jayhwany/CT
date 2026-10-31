import sys

def solve():
    # 입출력 속도 최적화
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    # parent[i]: i번 학생의 부모 노드 (초기에는 자기 자신이 대표)
    parent = list(range(n + 1))

    # Find 연산 (경로 압축 적용)
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # Union 연산
    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        # 서로 다른 그룹일 때만 하나로 합치고 True 반환
        if root_x != root_y:
            parent[root_y] = root_x
            return True
        return False

    # 처음엔 모든 학생(N명)이 서로 다른 종교를 가진 것으로 간주
    components = n
    idx = 2

    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2

        # 두 학생의 그룹을 합치는 데 성공하면 전체 그룹 수 -1
        if union(u, v):
            components -= 1

    print(components)

if __name__ == '__main__':
    solve()