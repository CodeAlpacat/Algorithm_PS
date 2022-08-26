from collections import deque
# input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, N = map(int, input().split())

mat = [list(map(int, list(input()))) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

def bfs(x, y):
    
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and not mat[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])
    
    

for i in range(N):
    bfs(0, i)

for i in range(N):
    if visited[M-1][i]:
        print('YES')
        break
else:
    print('NO')