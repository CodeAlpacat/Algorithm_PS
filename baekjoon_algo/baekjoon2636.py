import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]
dist = [[1000000000] * M for _ in range(N)] #가중치


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
                    
max_num = -1000000000
get_dist(0, 0, mat)
for i in dist:
    for j in i:
        if j > max_num:
            if j != 1000000000:
                max_num = j

cnt = 0
for i in dist:
    for j in i:
        if max_num == j:
            cnt += 1

print(max_num)
print(cnt)