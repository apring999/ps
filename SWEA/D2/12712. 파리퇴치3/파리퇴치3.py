T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    max_kill = 0
    # 상하좌우
    plus_dy = [-1, 1, 0, 0]
    plus_dx = [0, 0, -1, 1]
    # 대각선
    x_dy = [-1, -1, 1, 1]
    x_dx = [-1, 1, -1, 1]
 
    for i in range(N):
        for j in range(N):
            # + 모양 합산
            plus_sum = arr[i][j]
            for m in range(1, M):
                for d in range(4):
                    ny = i + plus_dy[d] * m
                    nx = j + plus_dx[d] * m
                    if 0 <= ny < N and 0 <= nx < N:
                        plus_sum += arr[ny][nx]
            # x 모양 합산
            x_sum = arr[i][j]
            for m in range(1, M):
                for d in range(4):
                    ny = i + x_dy[d] * m
                    nx = j + x_dx[d] * m
                    if 0 <= ny < N and 0 <= nx < N:
                        x_sum += arr[ny][nx]
            max_kill = max(max_kill, plus_sum, x_sum)
 
    print(f"#{tc} {max_kill}")