import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def get_dist(lst):
    pq =  []
    
    dist[0][0] = 0
    heapq.heappush(pq, (0, 0, 0))
    
    while pq:
        d, x, y = heapq.heappop(pq)
        
        if dist[x][y] != d:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                nd = dist[x][y] + lst[nx][ny]

                if dist[nx][ny] > nd:
                    dist[nx][ny] = nd
                    heapq.heappush(pq, (nd, nx, ny))
            

M, N = map(int, input().split())
mat = [list(map(int, list(input()))) for _ in range(N)]

dist = [[0xffffff] * M for _ in range(N)]

get_dist(mat)

print(dist[N-1][M-1])