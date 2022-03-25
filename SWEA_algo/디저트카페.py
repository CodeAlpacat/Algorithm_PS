
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
def dfs(x, y, dir, cnt):
    global ans

    if dir < 3:
        t = dir + 2
    else:
        t = dir + 1
    
    for i in range(dir, t):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if save[0] == nx and save[1] == ny:
            ans = max(ans, cnt)
            return
        
        if 0<= nx < N and 0 <= ny < N:
            if not visited[graph[nx][ny]]:
                visited[graph[nx][ny]] = True
                dfs(nx, ny, i, cnt + 1)
                visited[graph[nx][ny]] = False
    
T = int(input())
for tc in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * 101
    ans = -1
    for i in range(N):
        for j in range(N):
            save = [i, j]
            visited[graph[i][j]] = True
            dfs(i, j, 0, 1)
            visited[graph[i][j]] = False
    print(f'#{tc + 1} {ans}')