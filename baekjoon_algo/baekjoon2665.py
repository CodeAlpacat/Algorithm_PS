import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def get_dist():
    pq = []

    dist[0][0] = 0
    heapq.heappush(pq, [0, 0, 0])
    
    while pq:
        d, x, y = heapq.heappop(pq)
        
        if d != dist[x][y]:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                nd = d + mat[nx][ny]
                
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(pq, [nd, nx, ny])

N = int(input())
mat = [list(map(int, list(input()))) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if mat[i][j] == 1:
            mat[i][j] = 0
        else:
            mat[i][j] = 1

dist = [[0xffffff] * N for _ in range(N)]

get_dist()
print(dist[N-1][N-1])