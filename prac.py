N, M = map(int, input().split()) #세로 가로
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1,0, 1, 0]

visited = [[None] * M for _ in range(N)]
def dfs(x, y, d):
    room[x][y] = 2
    i = d + 1
    if d == 3:
        i = i % 4 
    for _ in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            dfs(nx, ny, i)
            break            
        i += 1
    else:
        if 