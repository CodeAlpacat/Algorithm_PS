import sys
# sys.stdin=open('sample_input.txt')

sys.setrecursionlimit(10000)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < M and 0 <= ny < N and mat[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)

M, N, K = map(int, input().split())
mat = [[1] * N for _ in range(M)]
li = [list(map(int, input().split())) for _ in range(K)]
visited = [[False] * N for _ in range(M)]


for i in range(M):
    for j in range(N):
        for k in li:
            if k[1] <= i < k[3] and k[0] <= j < k[2] and mat[i][j] == 1:
                mat[i][j] = 0
ans = []
cnt_area = 0
for i in range(M):
    for j in range(N):
        cnt = 0
        if mat[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            ans.append(cnt)
            cnt_area += 1

print(cnt_area)
print(*sorted(ans))