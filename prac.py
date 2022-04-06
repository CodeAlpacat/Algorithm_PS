# import sys
# sys.stdin=open('sample_input.txt')
from collections import deque


N, M = 6, 4

visited = [[0]*M for _ in range(N)]
def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] =True

    while q:
        x, y = q.popleft()

        if mat[x][y] == 2:
            ans = min(ans, )
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and mat[nx][ny] != 1:
                visited[nx][ny] =visited[x][y] + 1
                q.append([nx, ny])