from collections import deque


T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1 ,0]

def bfs(x, y, virus):
    visited[x][y] = True
    q = deque()
    q.append([x, y])
    cnt = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and mat[nx][ny] != '_':
                if mat[nx][ny] == virus:
                    q.append([nx, ny])
                    cnt += 1
                    visited[nx][ny] = True
    
    return cnt #최대 크기 미생물

for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(input()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    cnt_A = 0
    cnt_B = 0
    max_num = -1000000000
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            if mat[i][j] == '_':
                continue
            elif mat[i][j] == 'A':
                cnt_A += 1
                max_num = max(max_num, bfs(i, j, 'A'))
            elif mat[i][j] == 'B':
                cnt_B += 1
                max_num = max(max_num, bfs(i, j, 'B'))
    
    print(f'#{tc} {cnt_A} {cnt_B} {max_num}')
            