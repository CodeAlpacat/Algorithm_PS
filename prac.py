from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

mat = [list(input().split()) for _ in range (5)]
res = []
def dfs(x, y, cnt):
    cnt += mat[x][y]
    
    if len(cnt) == 6:
        if cnt not in res:
            res.append(cnt)
        return
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, cnt)

for i in range(5):
    for j in range(5):
        dfs(i, j, '')

print(len(res))