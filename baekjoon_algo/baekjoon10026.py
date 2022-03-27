# import sys
# sys.stdin=open('sample_input.txt')
import sys
sys.setrecursionlimit(1000000)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y):

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < N and not visited[nx][ny]:
            if mat[nx][ny] == mat[x][y]:
                DFS(nx, ny)
                  
    
N = int(input())
mat = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt = 0
cnt_no_color = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            DFS(i, j)
            cnt += 1

for i in range(N):
    for j in range(N):
        if mat[i][j] == 'R':
            mat[i][j] = 'G'
        visited[i][j] = False

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            DFS(i, j)
            cnt_no_color += 1

print(cnt, cnt_no_color)