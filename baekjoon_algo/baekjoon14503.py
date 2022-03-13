N, M = map(int, input().split()) #세로 가로
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dfs(x, y, d):
    room[x][y] = 2
    i = (d + 3) % 4
    for _ in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            dfs(nx, ny, i)
            return
        i = (i+3) % 4
    else:
        if room[x-dx[d]][y-dy[d]] == 1:
            return
        else:
            dfs(x-dx[d], y-dy[d], d)
            return


dfs(r, c, d)
cnt = 0
for i in range(N):
    # print(*room[i])
    for j in range(M):
        if room[i][j]==2:
            cnt += 1
print(cnt)