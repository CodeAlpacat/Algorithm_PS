T = int(input())
dx_odd = [0, 1, 1, 1, 0, -1]
dy_odd = [1, 1, 0, -1, -1, 0]

dx_even = [0, 1, 0, -1, -1, -1]
dy_even = [1, 0, -1, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < M and 0 <= y < N
def check():
    x, y = 0, 0
    for i in range(M*2):
        for j in range(N):
            if visited[i][j] == 1:
                x, y = i, j
                return (x, y)
def bfs():
    a = check()
    x, y = a[0], a[1]
    visited_new = [[0] * N for _ in range(M)]
    q = deque()
    q.append([x, y])
    visited_new[x][y] = mat[x][y]
    d = 0
    while q:
        
        for _ in range(len(q)):
            x, y = q.popleft()
            
            if d == 3:
                return True
            
            for i in range(6):
                if y % 2 == 0:
                    nx = x + dx_even[i]
                    ny = y + dy_even[i]
                else:
                    nx = x + dx_odd[i]
                    ny = y + dy_odd[i]
                
                if not in_range(nx, ny):
                    continue

                if not visited[nx][ny]:
                    continue

                if visited_new[nx][ny]:
                    continue
                
                visited_new[nx][ny] = True
                q.append([nx, ny])
        d += 1
    return False
        

def recur(x, y, cnt, total):
    global ans

    if cnt > 4:
        return

    if cnt == 4:
        if bfs():
            ans = max(ans, total)
        return

    if y == N:
        y = 0
        x += 1
    if x == M:
        return

    if mat[x][y] != -1 and not visited[x][y]:
        visited[x][y] = 1
        recur(x, y + 1, cnt + 1, total + mat[x][y])
        visited[x][y] = 0
    recur(x, y + 1, cnt, total)
    


for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [[0] * N for _ in range(M)]
    mat = [list(map(int, input().split())) for _ in range(M)]


    ans = -0xffffff
    recur(0, 0, 0, 0)
    

    print(f'#{tc} {ans**2}')





