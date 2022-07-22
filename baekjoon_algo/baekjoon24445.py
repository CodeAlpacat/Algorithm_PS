# import sys
from collections import deque

# input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    
    graph[u].append(v)
    graph[v].append(u)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    cnt = 1
    while q:
        n = q.popleft()
        graph[n].sort(reverse=True)
        for i in graph[n]:
            if visited[i]:
                continue
            cnt += 1
            visited[i] = cnt
            q.append(i)
bfs(R)
for i in visited[1:]:
    print(i)