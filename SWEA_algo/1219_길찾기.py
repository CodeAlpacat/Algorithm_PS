#길찾기
def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

for p in range(10):

    T, path = map(int, input().split())
    li = list(map(int, input().split()))

    visited = [False] * 100 # 0과 99가 포함되어있음.
    graph = [[] for _ in range(100)]
    for i in range(1, len(li)):
        if i % 2:
            graph[li[i-1]].append(li[i])

    dfs(graph, 0, visited)

    ans = 0
    if visited[99]:
        ans = 1

    print(f'#{T} {ans}')