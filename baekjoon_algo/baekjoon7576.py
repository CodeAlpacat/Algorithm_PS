from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

li = []
for i in range(M): #1의 위치 정보 리스트에 담기
    for j in range(N):
        if mat[i][j] == 1:
            li.append([i, j])


def bfs(lst):
    for i in range(len(lst)):
        visited[lst[i][0]][lst[i][1]] = True
    
    q = deque()
    for i in range(len(lst)):
        q.append([lst[i][0], lst[i][1]])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and mat[nx][ny] != -1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

def check():
    for i in range(M):
        for j in range(N):
            if visited[i][j] == 0 and mat[i][j] != -1:
                return True

flag = False
for i in range(M):
    for j in range(N):
        if mat[i][j] == 1 or mat[i][j] == -1:
            continue
        else:
            flag = False
            break
    if not flag:
        break
else:
    flag = True


if flag: #처음부터 다 익음.
    print(0)
else:
    bfs(li)
    if check():
        print(-1)
    else:
        max_num = -1000000000 
        for i in range(M):
           for j in range(N):
               if max_num < visited[i][j]:
                   max_num = visited[i][j]
        print(max_num - 1)