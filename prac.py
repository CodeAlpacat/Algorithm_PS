# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

input = sys.stdin.readline


#R, C로부터 거리가 D 이하인 칸들에 교통 정체
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    visited = [[0] * N for _ in range(M)]
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    
    d = 0
    while q:

        for _ in range(len(q)):
            a, b = q.popleft()

            if a == N and b == M:
                return d

            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not mat[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
        d += 1

def get_traffic(x, y, d):
    

N, M = map(int, input().split())
K = int(input())
mat = [[0] * N for _ in range(M)]

min_dist = -0xffffff
for i in range(K):
    R, C, D = map(int, input().split())
    

min_dist = min(min_dist, bfs(0, 0))
    
