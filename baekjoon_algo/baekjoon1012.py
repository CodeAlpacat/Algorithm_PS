# import sys
# sys.setrecursionlimit(100000)
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# def dfs(x, y):
#     visited[x][y] = True
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
#             if li[nx][ny]:
#                 dfs(nx, ny)

# T = int(input())
# for tc in range(T):
#     M, N, K = map(int, input().split())
#     li = [[0] * M for _ in range(N)]
#     visited = [[0] * M for _ in range(N)]
#     for i in range(K):
#         a, b = map(int, input().split())
#         li[b][a] = 1
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if li[i][j] and not visited[i][j]:
#                 dfs(i, j)
#                 cnt += 1
#     print(cnt)

from collections import deque


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y):
    visited[x][y] = True
    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if li[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return 1

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    li = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for i in range(K):
        a, b = map(int, input().split())
        li[b][a] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if li[i][j] and not visited[i][j]:
                cnt += dfs(i, j)
                
    print(cnt)