from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    min_node = A[v]
    while q:
        n = q.popleft()
        min_node = min(min_node, A[n])
        for i in graph[n]:
            if visited[i]:
                continue
            q.append(i)
            visited[i] = True
    return min_node

N, M, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)
    
ans = 0
for i in range(1, N+1):
    if visited[i]:
        continue
    else:
        ans += bfs(i)

if ans > k:
    print("Oh no")
else:
    print(ans) 