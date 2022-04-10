from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs(x, y):
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = True
    d = 1
    while q:
        size = len(q)

        for _ in range(size):
            x, y, crash = q.popleft()
            
            if x == N-1 and y == M-1:
                return d

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not in_range(nx, ny):
                    continue
                
                ncrash = crash + graph[nx][ny] # 벽이면 1씩 추가
                
                if ncrash > 1 or visited[nx][ny][ncrash]: # 방문했거나 벽을 두 번 부쉈으면 continue
                    continue
                q.append([nx, ny, ncrash])
                visited[nx][ny][ncrash] = True
    
        d += 1
    return -1

N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]
visited = [[[False] * 3 for _ in range(M)] for _ in range(N)] #3차원 배열과 벽을 0, 1, 2회 부쉈는지

print(bfs(0, 0))

# 6 4
# 0100
# 1110
# 1000
# 0100
# 0111
# 0000