T = int(input())

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]
def in_range(x, y):
    return 1 <= x <= N and 1 <= y <= N

def change(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny) or chess[nx][ny] == 0:
            continue
        if chess[nx][ny] == chess[x][y]:
            continue
        
        if check(x, y, nx, ny, i):
            while in_range(nx, ny) and chess[x][y] != chess[nx][ny]:
                if chess[nx][ny] == 0:
                    break
                if chess[nx][ny] == 1:
                    chess[nx][ny] = 2
                elif chess[nx][ny] == 2:
                    chess[nx][ny] = 1
                nx += dx[i]
                ny += dy[i]

def check(x, y, nx, ny, direction):
    while in_range(nx, ny) and chess[x][y] != chess[nx][ny]:
        if chess[nx][ny] == 0:
            return False
        nx += dx[direction]
        ny += dy[direction]
    if in_range(nx, ny) and chess[x][y] == chess[nx][ny]: #이미 한칸 떨어진건 지나옴.
        return True
    else:
        return False

for tc in range(T):
    N, M = map(int, input().split())
    chess = [[0] + [0 for _ in range(N)] for _ in range(N+1)]
    chess[N//2][N//2] = 2
    chess[N//2+1][N//2] =1
    chess[N//2][N//2+1] =1
    chess[N//2+1][N//2+1] =2

    for i in range(M):
        y, x, stone = map(int, input().split())
        chess[x][y] = stone
        change(x, y) #돌을 바꾸는 함수 check
    
    cnt_B = 0
    cnt_W = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if chess[i][j] == 1:
                cnt_B += 1
            
            if chess[i][j] == 2:
                cnt_W += 1

    print(f'#{tc+1} {cnt_B} {cnt_W}')