import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]
dist = [[0xffffff] * M for _ in range(N)] #가중치
copy_dist = [i[:] for i in mat]

def get_dist(x, y, v):
    pq = []
    
    dist[x][y] = 0
    heapq.heappush(pq, (0, x, y))
    while len(pq):
        d, cur_x, cur_y = heapq.heappop(pq)

        if dist[cur_x][cur_y] != d:
            continue

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                nxt_x, nxt_y = nx, ny
                nd = dist[cur_x][cur_y] + v[nx][ny]
                
                if dist[nxt_x][nxt_y] > nd:
                    dist[nxt_x][nxt_y] = nd
                    heapq.heappush(pq, (nd, nxt_x, nxt_y))

max_num = -0xffffff
get_dist(0, 0, mat)

for i in range(N):
    for j in range(M):
        if copy_dist[i][j] == 0:
            dist[i][j] = 0


for i in dist:
    for j in i:
        if j > max_num:
            if j != 0xffffff:
                max_num = j

cnt = 0
for i in dist:
    for j in i:
        if max_num == j:
            cnt += 1



print(max_num)
if max_num == 0:
    print(0)
else:
    print(cnt)