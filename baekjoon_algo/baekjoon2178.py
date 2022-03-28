from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def in_range(x, y):
    return 0 <= x < N and 0 <= y < M
def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    d = 1
    while q:

        for _ in range(len(q)):
            x, y = q.popleft()
            
            if x == N-1 and y == M-1:
                return d

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not in_range(nx, ny) or visited[nx][ny]:
                    continue
                
                if not mat[nx][ny]:
                    continue

                q.append([nx,ny])
                visited[nx][ny] = True
        d += 1
            
            
            

N, M = map(int, input().split())
mat = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

print(bfs())
