from collections import deque
# input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

#먹이들의 위치 파악
def find_pray(size):
    flag = False
    global shark_size, pray_cnt
    a = shark_now()
    distance = 0xffffff
    now = []
    if shark_size == pray_cnt:
        pray_cnt = 0
        shark_size += 1
    for i in range(len(mat)):
        for j in range(len(mat)):
            if size > mat[i][j] and mat[i][j]:
                if abs(a[0] - i) + abs(a[1] - j) < distance:
                    distance = abs(a[0] - i) + abs(a[1] - j)
                    now =[i, j]
                    flag = True
    if now:
        pray_list[now[0]][now[1]] = 1
    if flag:
        return 0
    else:
        return 1
def check_distance(shark_x, shark_y):
    global shark_size, pray_cnt, ans
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append([shark_x, shark_y])
    visited[shark_x][shark_y] = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and mat[nx][ny] <= shark_size:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    
    for j in range(N):
        for k in range(N):
            if pray_list[j][k]:
                ans += visited[j][k] - 1
                if pray_cnt >= shark_size:
                    pray_cnt = 0
                    shark_size += 1
                pray_cnt += 1
                mat[j][k] = 9
                mat[shark_x][shark_y] = 0
                find_pray(shark_size)
                return 1
    return 0


def reset_pray():
    for i in range(len(mat)):
        for j in range(len(mat)):
            pray_list[i][j] = 0

def shark_now():
    shark = []
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 9:
                shark = [i, j]
    return shark

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
pray_cnt = 0
shark_size = 2
pray_list = [[0] * N for _ in range(N)]
ans = 0




while True:
    reset_pray()
    new_flag = find_pray(shark_size)
    if new_flag:
        break
    shark_place = shark_now()
    check_distance(shark_place[0], shark_place[1])


print(ans)