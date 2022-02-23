#미로
# 중복없는 순열
def mazeDfs(x, y, visited):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if miro[nx][ny] == 3:
                return 1
            elif not miro[nx][ny]: #0이면 통로. 재귀로 들어감
                visited[nx][ny] = True
                if mazeDfs(nx, ny, visited):
                    return 1
            


T = int(input())

for t in range(T):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)] #2차원 배열 방문했는지
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                if mazeDfs(i, j, visited):
                    print(f'#{t+1} {1}')
                else:
                    print(f'#{t+1} {0}')