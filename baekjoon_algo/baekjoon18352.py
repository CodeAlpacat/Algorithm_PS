from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    
    while q:
        n = q.popleft()
        
        if visited[n]-1 == K:
            res.append(n)

        for i in mat[n]:
            if visited[i]:
                continue
            
            q.append(i)
            visited[i] = visited[n] + 1

N, M, K, X = map(int, input().split())
mat = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    s, e = map(int, input().split())
    mat[s].append(e)

res = []
bfs(X)

if len(res) == 0:
    print(-1)
else:
    for i in res:
        print(i)