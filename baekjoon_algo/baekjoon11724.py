
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i]:
            continue
        dfs(i)

N, M = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        ans += 1
    elif visited[i]:
        continue

print(ans)