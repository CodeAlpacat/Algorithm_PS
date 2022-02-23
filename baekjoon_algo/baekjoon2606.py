#2606 바이러스

N = int(input()) #컴퓨터 수
M = int(input()) #간선 수(입력 수)

def dfs_virus(v):
    global cnt
    visited[v] = True
    
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs_virus(i)

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
cnt = 0
dfs_virus(1)


print(cnt-1) #0번 빈리스트도 True임.