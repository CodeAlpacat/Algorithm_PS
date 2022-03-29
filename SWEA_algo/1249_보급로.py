from collections import deque
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not in_range(nx, ny):
                continue
            
            distance = mat[nx][ny] + visited[x][y] # 다음노드의 가중치 + 현재까지의 거리
            if distance < visited[nx][ny]:
                visited[nx][ny] = distance #다음 방문할 곳이 방문하지 않았거나 방문해도 거리가 더 긴가?
                q.append([nx, ny])

    return visited[N-1][N-1]
            
            

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[2000000000] * N for _ in range(N)]
    
    print(f'#{tc} {bfs()}')