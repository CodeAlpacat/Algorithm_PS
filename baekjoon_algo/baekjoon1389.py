from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq


def bfs(s):
    visited = [0] * (N+1)
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        s = q.popleft()
        
        for i in mat[s]:
            if visited[i]:
                continue
            
            q.append(i)
            visited[i] = visited[s] + 1
    return sum(visited) - N

N, M = map(int, input().split())

mat = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    
    mat[a].append(b)
    mat[b].append(a)

ans = 0xffffff
idx_ans = 0
for i in range(1, N+1):
    if ans > bfs(i):
        idx_ans = i
        ans = bfs(i)
    elif ans == bfs(i):
        if idx_ans > i:
            idx_ans = i
print(idx_ans)