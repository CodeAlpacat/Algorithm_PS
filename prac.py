# import sys
# sys.stdin=open('sample_input.txt')

from collections import deque
import heapq


T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1 ,0]

def get_dist():
    pq = []

    dist[0][0] = 0
    heapq.heappush(pq, (0, 0, 0))
    while len(pq):
        d, cur_x, cur_y = heapq.heappop(pq)
        
        if dist[cur_x][cur_y] != d:
            continue
        
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                num_cost = abs(mat[nx][ny] - mat[cur_x][cur_y]) + 1
                nxt = d + num_cost

                if dist[nx][ny] > nxt:
                    dist[nx][ny] = nxt
                    heapq.heappush(pq, (nxt, nx, ny))




for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    dist = [[1000000000] * N for _ in range(N)]
    get_dist()
    print(f'#{tc} {dist[N-1][N-1]}')