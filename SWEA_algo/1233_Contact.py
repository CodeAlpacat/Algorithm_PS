from collections import deque

def bfs(n):
    q = deque([n])
    visited[n] = True

    while q:
        v = q.popleft()
        
        for i in graph[v]:
            if visited[i]:
                continue
            q.append(i)
            visited[i] = visited[v] + 1
    

for tc in range(10):
    N, start = map(int, input().split())
    node_li = list(map(int, input().split()))
    graph = [[] for _ in range(102)]
    visited = [0] * 102
    for i in range(0, len(node_li)-1, 2):
        graph[node_li[i]].append(node_li[i+1])
    

    bfs(start)
    ans = 0
    ans_idx = 0
    for i in range(len(visited)):
        if visited[i] >= ans:
            ans = visited[i]
            ans_idx = max(ans_idx, i)

    print(f'#{tc+1} {ans_idx}')