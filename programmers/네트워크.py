def solution(n, computers):
    graph = [[] for _ in range(n)]
    visited = [False] * (n)
    
    for i in range(len(computers)):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)
    def dfs(v):
        visited[v] = True
        
        for i in graph[v]:
            if visited[i]:
                continue
            dfs(i)
    cnt = 0
    for i in range(n):
        if visited[i]:
            continue
        dfs(i)
        cnt += 1
    return cnt