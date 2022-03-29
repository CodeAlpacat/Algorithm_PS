from collections import deque


def bfs(v):
    global ans
    visited = [False] * (N+1)
    q = deque()
    q.append(v)
    visited[v] = True
    d = 1
    while q:
        for _ in range(len(q)):
            n = q.popleft()
            for i in graph[n]:
                if visited[i]:
                    continue
                visited[i] = True
                q.append(i)
                d += 1
    return d


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)
res = []
ans = -100000000
for i in range(1, N+1):
    a = bfs(i)
    if ans < a:
        ans = a
    res.append([i, a])

for i, a in res:
    if a == ans:
        print(i, end =' ')