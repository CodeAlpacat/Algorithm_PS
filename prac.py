
T = int(input())
dx = [0, 1, 0, -1, 1, -1, 1, -1]
dy = [1, 0, -1, 0, 1, 1, -1, -1]

def omok(x, y, n): #제자리가 o일 때 이므로 자기자신 고려 x
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        cnt = 1 #자기 자신.
        while 0 <= nx < n and 0 <= ny < n:
            if li[nx][ny] == 'o':
                cnt += 1
            elif cnt < 5 and li[nx][ny] == '.':
                break
            nx += dx[i]
            ny += dy[i]
        if cnt >= 5:
            return True
    else:
        return False
        

def check(N, li):
    for i in range(N):
        for j in range(N):
            if li[i][j] == 'o':
                if omok(i, j, N):
                    return True
    else:
        return False

for t in range(T):
    N = int(input())
    li = [list(input()) for _ in range(N)] # N * N 오목판
    
    if check(N, li):
        print(f'#{t+1} YES')
    else:
        print(f'#{t+1} NO')