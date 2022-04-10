# import sys
# sys.stdin=open('sample_input.txt')
from collections import deque
import heapq
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, dir):
    q.append([x, y, dir])
    visited[x][y][dir] = 1
    while q:
        x, y, dir= q.popleft()

        if x == end_x -1 and y == end_y -1 and dir == end_dir - 1:
            print(visited[x][y][dir]-1)
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and dir == i:
                k > 2:
                
    

        
        

N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]
start_x, start_y, start_dir = map(int, input().split())
end_x, end_y, end_dir = map(int, input().split())
visited = [[[0] * 4 for _ in range(N)]  for _ in range(M)]

q = deque()

bfs(start_x-1, start_y-1, start_dir-1)