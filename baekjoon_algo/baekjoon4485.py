import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def get_dist():
    pq = []
    
    dist[0][0] = 0
    heapq.heappush(pq, [0, 0, 0])

    while pq:
        d, cur_x, cur_y = heapq.heappop(pq)
        
        if dist[cur_x][cur_y] != d:
            continue

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                nd = dist[cur_x][cur_y] + mat[nx][ny]
                
                if dist[nx][ny] > nd:
                    dist[nx][ny] = nd
                    heapq.heappush(pq, (nd, nx, ny))

cnt = 0
while True:
    cnt += 1
    N = int(input())

    if not N:
        break

    mat = [list(map(int, input().split())) for _ in range(N)]
    dist = [[0xffffff] * N for _ in range(N)]
    get_dist()
    print(f'Problem {cnt}: {mat[0][0]+dist[N-1][N-1]}')