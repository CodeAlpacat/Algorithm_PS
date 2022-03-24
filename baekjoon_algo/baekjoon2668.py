cnt = 0
def dfs(cur, v):
    visited[cur] = True

    if graph[cur] == v:
        return True
    
    if visited[graph[cur]]:
        return False
    
    return dfs(graph[cur], v)


N = int(input())
ans = []
graph = [0 for _ in range(N+1)]
for i in range(1,N+1):
    node = int(input())
    graph[i] = node

for i in range(1, N+1):
    visited = [False] * (N+1)
    if dfs(i, i):
        cnt += 1
        ans.append(i)

print(cnt)
for i in ans:
    print(i)
