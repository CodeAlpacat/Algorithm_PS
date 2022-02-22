#그래프 경로

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

T = int(input())

for x in range(T):
    V, E = map(int, input().split()) #노드의 수, 간선의 수
    visited = [False] * (V+1) # 방문했는지 판별할 노드의 개수
    graph_v = [[] for _ in range(V+1)] # 노드는 1부터 시작하므로 0은 빈노드로
    for i in range(E):
        node, target = map(int, input().split()) #시작 노드와 이어진 도착 노드     
        graph_v[node].append(target) #순서대로 1번 ~ V번 노드까지 연결된 노드저장
    S, G = map(int, input().split()) # 출발 노드와 도착 노드
    
    dfs(graph_v, S, visited) #시작노드 = S
    ans = 0
    if visited[G]:
        ans = 1
    print(f'#{x+1} {ans}')