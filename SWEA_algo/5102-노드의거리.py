from collections import deque


T = int(input())

def bfs(s, g, visited):
    q = deque([s])
    visited[s] = 1

    while q:
        v = q.popleft()
        
        for i in g[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[v] + 1

for tc in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        node_from, node_to = map(int, input().split())
        graph[node_from].append(node_to) #무방향 그래프
        graph[node_to].append(node_from)
    S, G = map(int, input().split())
    
    bfs(S, graph, visited)
    if visited[G] != 0:
        print(f'#{tc+1} {visited[G] - 1}')
    else:
        print(f'#{tc+1} 0')