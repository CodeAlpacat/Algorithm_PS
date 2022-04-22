from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y, cnt):
    q = deque()
    q.append([x, y])
    mat[x][y] = cnt
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and mat[nx][ny] == 1:
                visited[nx][ny] =True
                mat[nx][ny] = cnt
                q.append([nx, ny])

def bfs_island(x, y, current_isalnd):
    visited_island = [[0] * N for _ in range(N)]
    visited_island[x][y] = True
    q = deque()
    q.append([x, y])
    d = 1
    while q:
        
        for _ in range(len(q)):

            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited_island[nx][ny] and mat[nx][ny] == 0:
                    visited_island[nx][ny] = True
                    q.append([nx, ny])
                if 0 <= nx < N and 0 <= ny < N and not visited_island[nx][ny] and mat[nx][ny] != current_isalnd and mat[nx][ny] != 0:
                    return d-1
        d += 1
    return 0xffffff

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


cnt = 1
for i in range(N):
    for j in range(N):
        if not visited[i][j] and mat[i][j] == 1:
            bfs(i, j, cnt)
            cnt += 1

ans = 0xffffff

for i in range(N):
    for j in range(N):
        if mat[i][j]:
            ans = min(ans, bfs_island(i, j, mat[i][j]))
        
print(ans)