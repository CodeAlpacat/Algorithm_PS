#2667 단지번호붙이기
dx = [0, 1, 0, -1] #우하좌상
dy = [1, 0, -1, 0]

def dfs_home(x, y, cnt):
    visited[x][y] = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if graph[nx][ny] == 1:
                visited[nx][ny] = cnt
                dfs_home(nx, ny, cnt)


def check(N):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                if not visited[i][j]:
                    cnt += 1
                    dfs_home(i, j, cnt)
    
    cnt_li = [0] * (cnt+1)
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                cnt_li[visited[i][j]] += 1

    return cnt_li

N = int(input())

visited = [[False] * N for _ in range(N)]
graph = [list(map(int, list(input()))) for _ in range(N)] # N *N 단지

res = sorted(check(N))
print(len(res)-1)
for i in range(1, len(res)):
    print(res[i])