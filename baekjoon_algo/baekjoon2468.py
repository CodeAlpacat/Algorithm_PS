from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    flooded_field[x][y] = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and not flooded_field[nx][ny]:
                flooded_field[nx][ny] = 1
                q.append([nx, ny])
    return 1
                
#최대 높이 구하기
max_height= -0xffffff
for i in mat:
    max_height = max(max(i), max_height)

#높이를 1씩 높히면서 영역의 개수를 구함
ans = 0
for hgt in range(max_height+1):
    #잠겨랏
    total_land = 0
    flooded_field = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mat[i][j] <= hgt:
                flooded_field[i][j] = 1
    
    for i in range(N):
        for j in range(N):
            if not flooded_field[i][j]:
                total_land += bfs(i, j)
    ans = max(ans, total_land)

print(ans)