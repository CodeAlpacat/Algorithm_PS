#연구소
from collections import deque
import sys
# sys.stdin=open('sample_input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

def bfs(): #복사된 배열을 받아서 바이러스 퍼트리기
    lst = [i[:] for i in mat]
    li = [i[:] for i in li_1]
    li = deque(li)
    while li:
        x, y = li.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] == 0:
                lst[nx][ny] = 2
                li.append([nx, ny])
    return lst

def check_max(lst): # 복사된 리스트에 있는 0의 개수 세기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 0:
                cnt += 1
    return cnt

def recur(x, y, cnt): #2차원 조합
    global ans
    if cnt > 3:
        return

    if cnt == 3:
        a = bfs()
        ans = max(ans, check_max(a))
        return
    
    if y == M:
        y = 0
        x += 1
    
    if x == N:
        return

    if mat[x][y] == 0:
        mat[x][y] = 1
        recur(x, y+1, cnt + 1)
        mat[x][y] = 0
    recur(x, y + 1, cnt)

li_1 = deque()
for i in range(N):
    for j in range(M):
        if mat[i][j] == 2:
            li_1.append([i, j])

ans = -1000000000
recur(0, 0, 0)
print(ans)