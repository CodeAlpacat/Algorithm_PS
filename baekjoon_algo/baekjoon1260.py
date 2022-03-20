from collections import deque


def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if visited[i]:
            continue
        dfs(i)

def bfs(v):
    q = deque([v])
    visited_bfs[v] = True
    while q:
        n = q.popleft()
        print(n, end= ' ')
        for i in graph[n]:
            if visited_bfs[i]:
                continue
            q.append(i)
            visited_bfs[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
visited_bfs = [False] * (N+1)
for i in range(M):
    node, target = map(int, input().split())
    graph[node].append(target)
    graph[target].append(node)
for i in range(N+1):
    graph[i].sort()

dfs(V)
print()
bfs(V)