from collections import deque


N, M = map(int, input().split()) #세로 가로
island = [list(input()) for _ in range(N)]


def bfs(x, y):
    visited =[[0] * (M) for _ in range(N)]
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    d = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                nx = x + i[0]
                ny = y + i[1]
                if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny]:
                    continue
                
                if island[nx][ny] == 'W':
                    continue
                
                q.append([nx, ny])
                visited[nx][ny] = True

        d += 1
    return d
        
ans = 0
for i in range(N):
    for j in range(M):
        if island[i][j] == 'W':
            continue
        a = bfs(i, j)
        if a > ans:
            ans = a

print(ans-1)