from collections import deque


T = int(input())

def bfs(x, y):
    dx = [-1, 0, 1, 0] # 상우하좌
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if maze[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                
                elif maze[nx][ny] == 3:
                    return visited[x][y]
    return 0

for tc in range(T):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 0
    flag = True
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                ans = bfs(i, j)
                flag = False
                break
        if not flag:
            break
    if ans != 0:
        print(f'#{tc+1} {ans-1}')
    else:
        print(f'#{tc+1} {ans}')