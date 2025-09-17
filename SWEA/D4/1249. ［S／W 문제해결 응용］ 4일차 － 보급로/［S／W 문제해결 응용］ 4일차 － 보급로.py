#import sys
#sys.stdin = open('1249_SW.txt')

# from collections import deque

# 하 우 상 좌 순서
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]

    D = [[int(1e6)] * N for _ in range(N)]
    D[0][0] = MAP[0][0]
    Q = []
    Q.append((0, 0))

    while Q:
        r, c = Q.pop(0)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr <= N-1 and 0 <= nc <= N-1:
                new_cost = D[r][c] + MAP[nr][nc]
                if D[nr][nc] > new_cost:
                    D[nr][nc] = new_cost
                    Q.append((nr, nc))

    print(f"#{tc} {D[N-1][N-1]}")