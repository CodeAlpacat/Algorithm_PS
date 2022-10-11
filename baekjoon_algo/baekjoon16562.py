from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    min_node = A[v]
    while q:
        n = q.popleft()
        min_node = min(min_node, A[n])
        for i in graph[n]:
            if visited[i]:
                continue
            q.append(i)
            visited[i] = True
    return min_node

N, M, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)
    
ans = 0
for i in range(1, N+1):
    if visited[i]:
        continue
    else:
        ans += bfs(i)

if ans > k:
    print("Oh no")
else:
    print(ans) 



def find_(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_(par[x])
        return par[x]

def union_(a, b):
    a = find_(a)
    b = find_(b)
    
    if a == b:
        return
    
    par[a] = b
    mat[b] = min(mat[a], mat[b])


n, m, k = map(int, input().split())
mat = [0] + list(map(int, input().split()))
par = [i for i in range(n+1)]
rnk = [0 for i in range(n+1)]
total = 0
for i in range(m):
    a, b = map(int, input().split())
    
    #친구들끼리는 같은 트리 내에 존재
    #가장 부모는 최소 비용만 가지고 있어야함
    union_(a, b)

visited = [0 for _ in range(n+1)]
for i in range(1, n+1):
    x = find_(i)

    if visited[x]:
        continue
    
    total += mat[x]
    visited[x] = 1
    
if total > k:
    print("Oh no")
else:
    print(total)
    