from collections import deque
T = 10
N = 16

#상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj, maze):


    # 방문 배열도 N * N 만큼 필요하다
    # i행 j열을 방문한적이 있다. visited[i][j] = 1
    # i행 j열을 방문한적이 없다. visited[i][j] = 0
    visited = [[0] * N for _ in range(N)]

    # 너비우선탐색에 사용할 큐
    # 다음에 방문할 위치를 차례대로 저장
    q = deque()

     # 시작 위치를 다음에 방문하겠다 라고 큐에 넣은 상태로 탐색 시작
    q.append((si, sj))
    visited[si][sj] = 1

 # 큐 안에 다음 탐색 지점이 남아있으면 계속 탐색
    while q:
        # 다음 방문 위치를 꺼내와라. (i, j)
        i, j = q.popleft()

        # (i, j)에 3이 쓰여 있으면 도착
        if maze[i][j] == 3:
            # 도착가능하다는 값을 나타내는 1을 return 하고 바로 함수 종료(모든 반복문도 종료)
            return 1

        # (i, j)와 인접한 방문 가능한 위치 탐색
        # 2차원배열은 상하좌우
        for d in range(4):
        # 상하좌우 중 d 방향으로 이동했을 때 다음 좌표 (ni, nj)
            ni = i + di[d]
            nj = j + dj[d]
            # 이 이동후 좌표가 2차원 배열의 범위 안인지 반드시 먼저 확인
            # (ni, nj) 위치에 벽이 없어야 이동 가능
            # 이전에 (ni, nj) 위치를 방문한적이 없어야 한다
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and not visited[ni][nj]:
                # 위에 있는 3가지 조건 만족시 (ni, nj) 방문 가능
                # 큐에 (ni, nj)는 다음에 방문할 것이라는 사실 저장(예약)
                q.append((ni, nj))
                # (ni, nj)는 방문했다고 표시
                visited[ni][nj] = 1
            # while 문 안에서 3이 쓰인 위치 (i, j)를 찾지 못한다면
            # while문은 종료가 되고 코드가 여기까지 실행이 된다  3은 도착 불가
    return 0

for tc in range(1, T + 1):
# 테스트케이스 번호 입력만 받고 저장 x
    input()

    # 미로의 정보 2차원배열, 16 * 16
    maze = [list(map(int, input())) for _ in range(N)]
    # 탐색을 시작할 위치
    si, sj =0, 0

    # 2가 써져있는 부분이 각 TC의 탐색 위치 되므로 반복문 돌면서 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
                break
    # 도착 가능 여부가 bfs() 함수의 결과
    answer = bfs(si, sj, maze)

    print(f"#{tc} {answer}")