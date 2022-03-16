#연구소
from collections import deque


N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
ans = 0 
def recur(cur):

    if cur > 3:
        return

    if cur == 3:
        virus_spread()
        return

    if cur == N:
        return    
    for i in range(N):
        for j in range(M):
            if li[i][j] == 0:
                li[i][j] = 1
                recur(cur + 1)
                li[i][j] = 0
            


    
def virus_spread():
    global max_ans
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    arr = [[0]* M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            arr[i][j] = li[i][j]

    li_virus = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                li_virus.append([i, j])

    while li_virus:
        x, y = li_virus[0][0], li_virus[0][1]
        li_virus.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    li_virus.append([nx, ny])
    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                result += 1
    max_ans = max(max_ans, result)

max_ans = 0
recur(0)
print(max_ans)