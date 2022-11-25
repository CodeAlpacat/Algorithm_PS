import sys
from collections import deque

input = sys.stdin.readline


#R, C로부터 거리가 D 이하인 칸들에 교통 정체
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    
    d = 0
    while q:

        for _ in range(len(q)):
            a, b = q.popleft()

            if a == N-1 and b == M-1:
                return d

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not mat[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
        d += 1
    return -1000000

N, M = map(int, input().split())
K = int(input())
mat = [[0] * M for _ in range(N)]
min_dist = 0xffffff

for i in range(K):
    R, C, D = map(int, input().split())
    
    for j in range(D+1):
        if R-D+j-1 >= 0:
            if C-j-1 >= 0:
                mat[R-D+j-1][C-j-1] = 1
            if C+j-1 <= M-1:
                mat[R-D+j-1][C+j-1] = 1
        if R+D-j-1 <= N-1:
            if C-j-1 >= 0:
                mat[R+D-j-1][C-j-1] = 1
            if C+j-1 <= M-1:
                mat[R+D-j-1][C+j-1] = 1
    
for i in mat:
    print(*i)
min_dist = min(min_dist, bfs(0, 0))

if min_dist < -100000:
    print("NO")
else:
    print("YES")
    print(min_dist)
