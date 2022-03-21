from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < M and 0 <= y < N

# def bfs():
#     q = deque()
#     q.append([0, 0])
#     visited[0][0] = True
#     d = 0
#     while q:
#         size = len(q)
#         for _ in range(size):
#             x, y = q.popleft()
            
#             if x == M-1 and y == N-1:
#                 d += 1

#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if not in_range(nx, ny):
#                     continue
                
#                 if graph[x][y] <= graph[nx][ny]:
#                     continue
                

#                 q.append([nx, ny])

#     return d

def dfs(x, y):
    if visited[x][y] != None:
        return visited[x][y]

    d = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny):
            continue
        
        if graph[x][y] <= graph[nx][ny]:
            continue

        d += dfs(nx, ny)
    
    visited[x][y] = d
    return visited[x][y]

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
visited = [[None] * N for _ in range(M)]
visited[M-1][N-1] = 1
print(dfs(0, 0))